#!/usr/bin/env python3
"""
Stripe Payment Integration for OASIS v3
Handles subscription management and payment processing
"""

import os
import stripe
from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize Stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = Flask(__name__)
CORS(app)

# Subscription plans configuration
SUBSCRIPTION_PLANS = {
    "basic": {
        "name": "Basic Plan",
        "price": 999,  # $9.99 in cents
        "currency": "usd",
        "interval": "month",
        "requests_limit": 100,
        "features": ["100 API requests/month", "Basic support", "Standard models"]
    },
    "pro": {
        "name": "Pro Plan", 
        "price": 2999,  # $29.99 in cents
        "currency": "usd",
        "interval": "month",
        "requests_limit": 1000,
        "features": ["1,000 API requests/month", "Priority support", "Premium models", "Analytics dashboard"]
    },
    "enterprise": {
        "name": "Enterprise Plan",
        "price": 9999,  # $99.99 in cents
        "currency": "usd", 
        "interval": "month",
        "requests_limit": -1,  # Unlimited
        "features": ["Unlimited API requests", "24/7 dedicated support", "Custom models", "Advanced analytics", "SLA guarantee"]
    }
}

@app.route("/api/subscription/plans", methods=["GET"])
def get_subscription_plans():
    """Get available subscription plans"""
    return jsonify({"plans": SUBSCRIPTION_PLANS})

@app.route("/api/subscription/create-checkout-session", methods=["POST"])
def create_checkout_session():
    """Create a Stripe checkout session for subscription"""
    try:
        data = request.get_json()
        plan_id = data.get("plan_id")
        user_id = data.get("user_id")
        success_url = data.get("success_url", "https://your-frontend-url.vercel.app/success")
        cancel_url = data.get("cancel_url", "https://your-frontend-url.vercel.app/cancel")
        
        if plan_id not in SUBSCRIPTION_PLANS:
            return jsonify({"error": "Invalid plan ID"}), 400
        
        plan = SUBSCRIPTION_PLANS[plan_id]
        
        # Create or retrieve Stripe price
        try:
            # Try to find existing price
            prices = stripe.Price.list(
                product_data={"name": plan["name"]},
                unit_amount=plan["price"],
                currency=plan["currency"],
                recurring={"interval": plan["interval"]}
            )
            
            if prices.data:
                price_id = prices.data[0].id
            else:
                # Create new price
                price = stripe.Price.create(
                    unit_amount=plan["price"],
                    currency=plan["currency"],
                    recurring={"interval": plan["interval"]},
                    product_data={"name": plan["name"]}
                )
                price_id = price.id
                
        except Exception as e:
            return jsonify({"error": f"Failed to create price: {str(e)}"}), 500
        
        # Create checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price": price_id,
                "quantity": 1,
            }],
            mode="subscription",
            success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=cancel_url,
            client_reference_id=user_id,
            metadata={
                "plan_id": plan_id,
                "user_id": user_id
            }
        )
        
        return jsonify({"checkout_url": session.url, "session_id": session.id})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/subscription/webhook", methods=["POST"])
def stripe_webhook():
    """Handle Stripe webhooks for subscription events"""
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
    
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError:
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError:
        return jsonify({"error": "Invalid signature"}), 400
    
    # Handle the event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        handle_successful_payment(session)
        
    elif event["type"] == "invoice.payment_succeeded":
        invoice = event["data"]["object"]
        handle_successful_subscription_payment(invoice)
        
    elif event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        handle_subscription_cancellation(subscription)
        
    elif event["type"] == "invoice.payment_failed":
        invoice = event["data"]["object"]
        handle_failed_payment(invoice)
    
    return jsonify({"status": "success"})

def handle_successful_payment(session):
    """Handle successful initial payment"""
    user_id = session.get("client_reference_id")
    plan_id = session["metadata"].get("plan_id")
    
    # Update user subscription in Supabase
    # This would integrate with your existing Supabase setup
    print(f"User {user_id} successfully subscribed to {plan_id}")
    
    # You would add code here to:
    # 1. Update user subscription status in Supabase
    # 2. Grant access to premium features
    # 3. Send welcome email
    # 4. Update usage limits

def handle_successful_subscription_payment(invoice):
    """Handle successful recurring payment"""
    customer_id = invoice["customer"]
    subscription_id = invoice["subscription"]
    
    # Extend subscription period
    print(f"Subscription {subscription_id} payment successful")
    
    # You would add code here to:
    # 1. Reset monthly usage counters
    # 2. Extend subscription period
    # 3. Send payment confirmation

def handle_subscription_cancellation(subscription):
    """Handle subscription cancellation"""
    customer_id = subscription["customer"]
    
    # Downgrade user to free tier
    print(f"Subscription cancelled for customer {customer_id}")
    
    # You would add code here to:
    # 1. Downgrade user to free tier
    # 2. Restrict access to premium features
    # 3. Send cancellation confirmation

def handle_failed_payment(invoice):
    """Handle failed payment"""
    customer_id = invoice["customer"]
    
    # Handle payment failure
    print(f"Payment failed for customer {customer_id}")
    
    # You would add code here to:
    # 1. Send payment failure notification
    # 2. Retry payment or suspend account
    # 3. Update subscription status

@app.route("/api/subscription/portal", methods=["POST"])
def create_customer_portal():
    """Create Stripe customer portal session"""
    try:
        data = request.get_json()
        customer_id = data.get("customer_id")
        return_url = data.get("return_url", "https://your-frontend-url.vercel.app/dashboard")
        
        session = stripe.billing_portal.Session.create(
            customer=customer_id,
            return_url=return_url,
        )
        
        return jsonify({"portal_url": session.url})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/subscription/usage", methods=["POST"])
def track_api_usage():
    """Track API usage for billing purposes"""
    try:
        data = request.get_json()
        user_id = data.get("user_id")
        service_type = data.get("service_type")
        usage_count = data.get("usage_count", 1)
        
        # This would integrate with your existing usage tracking
        # and check against subscription limits
        
        # Example usage tracking logic:
        # 1. Get user's current subscription plan
        # 2. Check current usage against limits
        # 3. Allow or deny request based on limits
        # 4. Record usage in database
        
        return jsonify({
            "status": "success",
            "usage_recorded": usage_count,
            "remaining_requests": 950  # Example
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

