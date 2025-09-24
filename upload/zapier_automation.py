#!/usr/bin/env python3
"""
Zapier/Make.com Automation Integration for OASIS v3
Handles operational and marketing automation workflows
"""

import os
import requests
import json
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

class AutomationManager:
    def __init__(self):
        self.zapier_webhook_url = os.getenv("ZAPIER_WEBHOOK_URL")
        self.make_webhook_url = os.getenv("MAKE_WEBHOOK_URL")
        self.slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        self.telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.mailchimp_api_key = os.getenv("MAILCHIMP_API_KEY")
        self.mailchimp_list_id = os.getenv("MAILCHIMP_LIST_ID")

    def send_webhook(self, url, data):
        """Send data to webhook URL"""
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            return {"success": True, "response": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def notify_new_user(self, user_data):
        """Notify about new user registration"""
        notification_data = {
            "event_type": "new_user_registration",
            "timestamp": datetime.now().isoformat(),
            "user_id": user_data.get("user_id"),
            "email": user_data.get("email"),
            "signup_source": user_data.get("source", "website"),
            "plan": user_data.get("plan", "free")
        }

        # Send to Slack
        self.send_slack_notification(
            f"🎉 New user registered: {user_data.get('email')} (Plan: {user_data.get('plan', 'free')})"
        )

        # Send to Telegram
        self.send_telegram_notification(
            f"🎉 New OASIS user: {user_data.get('email')}\nPlan: {user_data.get('plan', 'free')}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        # Trigger Zapier workflow
        if self.zapier_webhook_url:
            self.send_webhook(self.zapier_webhook_url, notification_data)

        # Trigger Make.com workflow
        if self.make_webhook_url:
            self.send_webhook(self.make_webhook_url, notification_data)

        return notification_data

    def handle_paid_customer(self, payment_data):
        """Handle new paid customer automation"""
        customer_data = {
            "event_type": "new_paid_customer",
            "timestamp": datetime.now().isoformat(),
            "customer_id": payment_data.get("customer_id"),
            "email": payment_data.get("email"),
            "plan": payment_data.get("plan"),
            "amount": payment_data.get("amount"),
            "currency": payment_data.get("currency", "USD")
        }

        # Add to Mailchimp premium list
        self.add_to_mailchimp_list(
            email=payment_data.get("email"),
            merge_fields={
                "FNAME": payment_data.get("first_name", ""),
                "LNAME": payment_data.get("last_name", ""),
                "PLAN": payment_data.get("plan"),
                "AMOUNT": payment_data.get("amount")
            },
            tags=["paid_customer", f"plan_{payment_data.get('plan')}"]
        )

        # Grant premium access in Supabase
        self.grant_premium_access(
            user_id=payment_data.get("customer_id"),
            plan=payment_data.get("plan")
        )

        # Send welcome email sequence trigger
        self.trigger_welcome_sequence(payment_data.get("email"), payment_data.get("plan"))

        # Notify team
        self.send_slack_notification(
            f"💰 New paid customer: {payment_data.get('email')} - {payment_data.get('plan')} plan (${payment_data.get('amount')})"
        )

        return customer_data

    def send_slack_notification(self, message):
        """Send notification to Slack"""
        if not self.slack_webhook_url:
            return {"success": False, "error": "Slack webhook URL not configured"}

        payload = {
            "text": message,
            "username": "OASIS Bot",
            "icon_emoji": ":robot_face:",
            "channel": "#oasis-notifications"
        }

        return self.send_webhook(self.slack_webhook_url, payload)

    def send_telegram_notification(self, message):
        """Send notification to Telegram"""
        if not self.telegram_bot_token or not self.telegram_chat_id:
            return {"success": False, "error": "Telegram credentials not configured"}

        url = f"https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage"
        payload = {
            "chat_id": self.telegram_chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            response.raise_for_status()
            return {"success": True, "response": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def add_to_mailchimp_list(self, email, merge_fields=None, tags=None):
        """Add subscriber to Mailchimp list"""
        if not self.mailchimp_api_key or not self.mailchimp_list_id:
            return {"success": False, "error": "Mailchimp credentials not configured"}

        # Extract datacenter from API key
        datacenter = self.mailchimp_api_key.split('-')[-1]
        url = f"https://{datacenter}.api.mailchimp.com/3.0/lists/{self.mailchimp_list_id}/members"

        payload = {
            "email_address": email,
            "status": "subscribed",
            "merge_fields": merge_fields or {},
            "tags": tags or []
        }

        headers = {
            "Authorization": f"Bearer {self.mailchimp_api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            return {"success": True, "response": response.json()}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def grant_premium_access(self, user_id, plan):
        """Grant premium access in Supabase"""
        # This would integrate with your Supabase client
        # For now, we'll simulate the database update
        
        access_data = {
            "user_id": user_id,
            "plan": plan,
            "premium_access": True,
            "updated_at": datetime.now().isoformat()
        }

        # In a real implementation, you would:
        # 1. Update user record in Supabase
        # 2. Set appropriate permissions
        # 3. Update API rate limits
        # 4. Enable premium features

        print(f"Granted {plan} access to user {user_id}")
        return access_data

    def trigger_welcome_sequence(self, email, plan):
        """Trigger welcome email sequence"""
        sequence_data = {
            "event_type": "trigger_welcome_sequence",
            "email": email,
            "plan": plan,
            "timestamp": datetime.now().isoformat()
        }

        # This would trigger an email automation in your email service
        # For example, sending to Zapier to trigger a Mailchimp automation
        
        if self.zapier_webhook_url:
            self.send_webhook(self.zapier_webhook_url, sequence_data)

        return sequence_data

    def handle_churn_risk(self, user_data):
        """Handle users at risk of churning"""
        churn_data = {
            "event_type": "churn_risk_detected",
            "user_id": user_data.get("user_id"),
            "email": user_data.get("email"),
            "last_activity": user_data.get("last_activity"),
            "risk_score": user_data.get("risk_score"),
            "timestamp": datetime.now().isoformat()
        }

        # Trigger retention campaign
        self.trigger_retention_campaign(user_data.get("email"), user_data.get("risk_score"))

        # Notify customer success team
        self.send_slack_notification(
            f"⚠️ Churn risk detected: {user_data.get('email')} (Risk score: {user_data.get('risk_score')})"
        )

        return churn_data

    def trigger_retention_campaign(self, email, risk_score):
        """Trigger retention email campaign"""
        campaign_data = {
            "event_type": "trigger_retention_campaign",
            "email": email,
            "risk_score": risk_score,
            "timestamp": datetime.now().isoformat()
        }

        # Send to automation platform
        if self.zapier_webhook_url:
            self.send_webhook(self.zapier_webhook_url, campaign_data)

        return campaign_data

# Initialize automation manager
automation_manager = AutomationManager()

# API Endpoints
@app.route("/api/automation/new-user", methods=["POST"])
def handle_new_user():
    """Handle new user registration automation"""
    try:
        user_data = request.get_json()
        result = automation_manager.notify_new_user(user_data)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/automation/paid-customer", methods=["POST"])
def handle_new_paid_customer():
    """Handle new paid customer automation"""
    try:
        payment_data = request.get_json()
        result = automation_manager.handle_paid_customer(payment_data)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/automation/churn-risk", methods=["POST"])
def handle_churn_risk():
    """Handle churn risk automation"""
    try:
        user_data = request.get_json()
        result = automation_manager.handle_churn_risk(user_data)
        return jsonify({"status": "success", "data": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/automation/test-notification", methods=["POST"])
def test_notification():
    """Test notification systems"""
    try:
        data = request.get_json()
        message = data.get("message", "Test notification from OASIS v3")
        
        slack_result = automation_manager.send_slack_notification(message)
        telegram_result = automation_manager.send_telegram_notification(message)
        
        return jsonify({
            "status": "success",
            "slack": slack_result,
            "telegram": telegram_result
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/automation/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "integrations": {
            "zapier": bool(automation_manager.zapier_webhook_url),
            "make": bool(automation_manager.make_webhook_url),
            "slack": bool(automation_manager.slack_webhook_url),
            "telegram": bool(automation_manager.telegram_bot_token),
            "mailchimp": bool(automation_manager.mailchimp_api_key)
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

