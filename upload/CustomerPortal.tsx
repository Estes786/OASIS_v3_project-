import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { 
  UserCircleIcon, 
  CreditCardIcon, 
  DocumentTextIcon, 
  ChartBarIcon,
  CogIcon,
  BellIcon,
  ShieldCheckIcon,
  DownloadIcon,
  EyeIcon
} from '@heroicons/react/24/outline'

interface Customer {
  id: string
  name: string
  email: string
  plan: string
  usage: {
    api_calls: number
    monthly_limit: number
  }
  billing: {
    next_payment: string
    amount: number
    card_last4: string
  }
  account_status: 'active' | 'suspended' | 'trial'
}

interface ApiUsage {
  date: string
  calls: number
  cost: number
}

export default function CustomerPortal() {
  const [customer, setCustomer] = useState<Customer | null>(null)
  const [apiUsage, setApiUsage] = useState<ApiUsage[]>([])
  const [activeTab, setActiveTab] = useState('overview')

  useEffect(() => {
    fetchCustomerData()
    fetchApiUsage()
  }, [])

  const fetchCustomerData = async () => {
    try {
      const response = await fetch('/api/customer/profile')
      if (response.ok) {
        const data = await response.json()
        setCustomer(data)
      }
    } catch (error) {
      console.error('Error fetching customer data:', error)
    }
  }

  const fetchApiUsage = async () => {
    try {
      const response = await fetch('/api/customer/usage')
      if (response.ok) {
        const data = await response.json()
        setApiUsage(data)
      }
    } catch (error) {
      console.error('Error fetching API usage:', error)
    }
  }

  const downloadInvoice = async (invoiceId: string) => {
    try {
      const response = await fetch(`/api/customer/invoice/${invoiceId}`)
      if (response.ok) {
        const blob = await response.blob()
        const url = window.URL.createObjectURL(blob)
        const a = document.createElement('a')
        a.href = url
        a.download = `invoice-${invoiceId}.pdf`
        document.body.appendChild(a)
        a.click()
        window.URL.revokeObjectURL(url)
      }
    } catch (error) {
      console.error('Error downloading invoice:', error)
    }
  }

  if (!customer) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-600"></div>
      </div>
    )
  }

  const usagePercentage = (customer.usage.api_calls / customer.usage.monthly_limit) * 100

  return (
    <div className="max-w-7xl mx-auto px-4 py-8">
      {/* Customer Header */}
      <div className="bg-gradient-to-r from-purple-600 to-blue-600 rounded-xl p-8 text-white mb-8">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <UserCircleIcon className="h-16 w-16" />
            <div>
              <h1 className="text-3xl font-bold">{customer.name}</h1>
              <p className="text-purple-100">{customer.email}</p>
              <div className="flex items-center space-x-2 mt-2">
                <span className={`px-3 py-1 rounded-full text-sm font-medium ${
                  customer.account_status === 'active' 
                    ? 'bg-green-500 text-white'
                    : customer.account_status === 'trial'
                    ? 'bg-yellow-500 text-white'  
                    : 'bg-red-500 text-white'
                }`}>
                  {customer.account_status.toUpperCase()}
                </span>
                <span className="bg-white bg-opacity-20 px-3 py-1 rounded-full text-sm font-medium">
                  {customer.plan} Plan
                </span>
              </div>
            </div>
          </div>
          <div className="text-right">
            <p className="text-purple-100">Next Payment</p>
            <p className="text-2xl font-bold">${customer.billing.amount}</p>
            <p className="text-purple-100">{customer.billing.next_payment}</p>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="flex space-x-1 mb-8">
        {[
          { id: 'overview', label: 'Overview', icon: ChartBarIcon },
          { id: 'usage', label: 'API Usage', icon: EyeIcon },
          { id: 'billing', label: 'Billing', icon: CreditCardIcon },
          { id: 'settings', label: 'Settings', icon: CogIcon }
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-medium transition-colors ${
              activeTab === tab.id
                ? 'bg-purple-600 text-white'
                : 'text-gray-600 hover:bg-gray-100'
            }`}
          >
            <tab.icon className="h-5 w-5" />
            <span>{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Main Content */}
        <div className="lg:col-span-2">
          {activeTab === 'overview' && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="space-y-6"
            >
              {/* Usage Overview */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Current Usage</h2>
                <div className="space-y-4">
                  <div className="flex justify-between items-center">
                    <span className="text-gray-600">API Calls This Month</span>
                    <span className="font-semibold">
                      {customer.usage.api_calls.toLocaleString()} / {customer.usage.monthly_limit.toLocaleString()}
                    </span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-3">
                    <div 
                      className={`h-3 rounded-full ${
                        usagePercentage > 90 ? 'bg-red-500' : 
                        usagePercentage > 75 ? 'bg-yellow-500' : 'bg-green-500'
                      }`}
                      style={{ width: `${Math.min(usagePercentage, 100)}%` }}
                    />
                  </div>
                  <p className="text-sm text-gray-500">
                    {usagePercentage.toFixed(1)}% of monthly limit used
                  </p>
                </div>
              </div>

              {/* Recent Activity */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Recent Activity</h2>
                <div className="space-y-3">
                  {apiUsage.slice(0, 5).map((usage, index) => (
                    <div key={index} className="flex justify-between items-center py-2 border-b border-gray-100">
                      <div>
                        <span className="font-medium text-gray-900">{usage.calls} API calls</span>
                        <p className="text-sm text-gray-500">{usage.date}</p>
                      </div>
                      <span className="text-green-600 font-semibold">${usage.cost.toFixed(2)}</span>
                    </div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}

          {activeTab === 'usage' && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="bg-white rounded-xl shadow-lg p-6"
            >
              <h2 className="text-xl font-semibold text-gray-900 mb-4">Detailed Usage Analytics</h2>
              <div className="overflow-x-auto">
                <table className="min-w-full divide-y divide-gray-200">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Date
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        API Calls
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Cost
                      </th>
                      <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                        Status
                      </th>
                    </tr>
                  </thead>
                  <tbody className="bg-white divide-y divide-gray-200">
                    {apiUsage.map((usage, index) => (
                      <tr key={index}>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          {usage.date}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                          {usage.calls.toLocaleString()}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-sm text-green-600 font-semibold">
                          ${usage.cost.toFixed(2)}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className="px-2 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800">
                            Processed
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </motion.div>
          )}

          {activeTab === 'billing' && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="space-y-6"
            >
              {/* Payment Method */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Payment Method</h2>
                <div className="flex items-center justify-between p-4 border border-gray-200 rounded-lg">
                  <div className="flex items-center space-x-3">
                    <CreditCardIcon className="h-8 w-8 text-gray-400" />
                    <div>
                      <p className="font-medium text-gray-900">**** **** **** {customer.billing.card_last4}</p>
                      <p className="text-sm text-gray-500">Expires 12/25</p>
                    </div>
                  </div>
                  <button className="text-purple-600 hover:text-purple-700 font-medium">
                    Update
                  </button>
                </div>
              </div>

              {/* Invoice History */}
              <div className="bg-white rounded-xl shadow-lg p-6">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Invoice History</h2>
                <div className="space-y-3">
                  {[1, 2, 3, 4, 5].map((invoice) => (
                    <div key={invoice} className="flex justify-between items-center p-4 border border-gray-100 rounded-lg">
                      <div>
                        <p className="font-medium text-gray-900">Invoice #{invoice.toString().padStart(4, '0')}</p>
                        <p className="text-sm text-gray-500">September {invoice}, 2024</p>
                      </div>
                      <div className="flex items-center space-x-4">
                        <span className="text-green-600 font-semibold">${customer.billing.amount}</span>
                        <button
                          onClick={() => downloadInvoice(invoice.toString())}
                          className="text-purple-600 hover:text-purple-700"
                        >
                          <DownloadIcon className="h-5 w-5" />
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </motion.div>
          )}
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Quick Actions */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Quick Actions</h3>
            <div className="space-y-3">
              <button className="w-full flex items-center justify-center space-x-2 bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition-colors">
                <CreditCardIcon className="h-5 w-5" />
                <span>Upgrade Plan</span>
              </button>
              <button className="w-full flex items-center justify-center space-x-2 border border-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-50 transition-colors">
                <DocumentTextIcon className="h-5 w-5" />
                <span>View API Docs</span>
              </button>
              <button className="w-full flex items-center justify-center space-x-2 border border-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-50 transition-colors">
                <ShieldCheckIcon className="h-5 w-5" />
                <span>Generate API Key</span>
              </button>
            </div>
          </div>

          {/* Support */}
          <div className="bg-white rounded-xl shadow-lg p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Support</h3>
            <div className="space-y-3">
              <p className="text-sm text-gray-600">Need help? Our team is here to assist you.</p>
              <button className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors">
                Contact Support
              </button>
              <button className="w-full border border-gray-300 text-gray-700 py-2 px-4 rounded-lg hover:bg-gray-50 transition-colors">
                View Documentation
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}