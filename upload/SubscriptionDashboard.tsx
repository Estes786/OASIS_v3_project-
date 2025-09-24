import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  CurrencyDollarIcon, 
  ChartBarIcon, 
  UsersIcon, 
  CreditCardIcon,
  CheckCircleIcon,
  ExclamationTriangleIcon,
  ArrowTrendingUpIcon
} from '@heroicons/react/24/outline'

interface SubscriptionPlan {
  id: string
  name: string
  price: number
  features: string[]
  current: boolean
  popular?: boolean
}

interface SubscriptionMetrics {
  monthly_revenue: number
  active_subscribers: number
  churn_rate: number
  growth_rate: number
}

export default function SubscriptionDashboard() {
  const [metrics, setMetrics] = useState<SubscriptionMetrics>({
    monthly_revenue: 0,
    active_subscribers: 0,
    churn_rate: 0,
    growth_rate: 0
  })

  const [plans] = useState<SubscriptionPlan[]>([
    {
      id: 'starter',
      name: 'AI Starter',
      price: 29,
      features: [
        '1,000 AI API calls/month',
        'Basic sentiment analysis',
        'Text generation',
        'Email support'
      ],
      current: false
    },
    {
      id: 'professional',
      name: 'AI Professional',
      price: 99,
      features: [
        '10,000 AI API calls/month',
        'Advanced AI models',
        'Custom integrations',
        'Priority support',
        'Revenue analytics'
      ],
      current: true,
      popular: true
    },
    {
      id: 'enterprise',
      name: 'AI Enterprise',
      price: 299,
      features: [
        'Unlimited AI API calls',
        'Custom AI model training',
        'Dedicated support',
        'White-label solution',
        'Advanced analytics',
        'Quantum optimization'
      ],
      current: false
    }
  ])

  useEffect(() => {
    // Fetch real subscription metrics
    fetchSubscriptionMetrics()
  }, [])

  const fetchSubscriptionMetrics = async () => {
    try {
      const response = await fetch('/api/subscription-metrics')
      if (response.ok) {
        const data = await response.json()
        setMetrics(data)
      }
    } catch (error) {
      console.error('Error fetching metrics:', error)
    }
  }

  const upgradePlan = async (planId: string) => {
    try {
      const response = await fetch('/api/upgrade-plan', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ planId })
      })

      if (response.ok) {
        // Handle successful upgrade
        window.location.href = '/payment/upgrade'
      }
    } catch (error) {
      console.error('Upgrade error:', error)
    }
  }

  return (
    <div className="space-y-8">
      {/* Revenue Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Monthly Revenue</p>
              <p className="text-3xl font-bold text-green-600">
                ${metrics.monthly_revenue.toLocaleString()}
              </p>
            </div>
            <CurrencyDollarIcon className="h-8 w-8 text-green-500" />
          </div>
          <div className="mt-2 flex items-center text-sm">
            <ArrowTrendingUpIcon className="h-4 w-4 text-green-500 mr-1" />
            <span className="text-green-600">+{metrics.growth_rate}% this month</span>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Active Subscribers</p>
              <p className="text-3xl font-bold text-blue-600">
                {metrics.active_subscribers.toLocaleString()}
              </p>
            </div>
            <UsersIcon className="h-8 w-8 text-blue-500" />
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Churn Rate</p>
              <p className="text-3xl font-bold text-orange-600">
                {metrics.churn_rate}%
              </p>
            </div>
            <ChartBarIcon className="h-8 w-8 text-orange-500" />
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="bg-white rounded-xl shadow-lg p-6 border border-gray-200"
        >
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Projected Annual</p>
              <p className="text-3xl font-bold text-purple-600">
                ${(metrics.monthly_revenue * 12).toLocaleString()}
              </p>
            </div>
            <CreditCardIcon className="h-8 w-8 text-purple-500" />
          </div>
        </motion.div>
      </div>

      {/* Subscription Plans */}
      <div className="bg-white rounded-xl shadow-lg p-8">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Subscription Plans</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {plans.map((plan, index) => (
            <motion.div
              key={plan.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`relative rounded-xl border-2 p-6 ${
                plan.current 
                  ? 'border-blue-500 bg-blue-50' 
                  : plan.popular 
                  ? 'border-purple-500 bg-gradient-to-br from-purple-50 to-pink-50'
                  : 'border-gray-200 bg-white'
              }`}
            >
              {plan.popular && (
                <div className="absolute -top-3 left-1/2 transform -translate-x-1/2">
                  <span className="bg-purple-500 text-white px-3 py-1 rounded-full text-sm font-medium">
                    Most Popular
                  </span>
                </div>
              )}

              <div className="text-center">
                <h3 className="text-lg font-semibold text-gray-900">{plan.name}</h3>
                <div className="mt-2">
                  <span className="text-4xl font-bold text-gray-900">${plan.price}</span>
                  <span className="text-gray-500">/month</span>
                </div>
              </div>

              <ul className="mt-6 space-y-3">
                {plan.features.map((feature, idx) => (
                  <li key={idx} className="flex items-center">
                    <CheckCircleIcon className="h-5 w-5 text-green-500 mr-2" />
                    <span className="text-sm text-gray-600">{feature}</span>
                  </li>
                ))}
              </ul>

              <div className="mt-8">
                {plan.current ? (
                  <button className="w-full bg-gray-200 text-gray-800 py-2 px-4 rounded-lg font-medium cursor-not-allowed">
                    Current Plan
                  </button>
                ) : (
                  <button
                    onClick={() => upgradePlan(plan.id)}
                    className={`w-full py-2 px-4 rounded-lg font-medium transition-colors ${
                      plan.popular
                        ? 'bg-purple-600 hover:bg-purple-700 text-white'
                        : 'bg-blue-600 hover:bg-blue-700 text-white'
                    }`}
                  >
                    Upgrade to {plan.name}
                  </button>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  )
}