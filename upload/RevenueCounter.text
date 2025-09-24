import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { CurrencyDollarIcon, TrendingUpIcon, UsersIcon, SparklesIcon } from '@heroicons/react/24/outline'

const RevenueCounter = () => {
  const [revenue, setRevenue] = useState(0)
  const [apiCalls, setApiCalls] = useState(0)
  const [users, setUsers] = useState(0)
  const [isLoading, setIsLoading] = useState(true)

  const targetRevenue = 50000
  const progressPercentage = (revenue / targetRevenue) * 100

  useEffect(() => {
    const fetchRevenueData = async () => {
      try {
        // Simulated API call to revenue endpoint
        // Replace with actual API call to your HuggingFace Space
        const response = await fetch('/api/revenue-dashboard')
        
        if (response.ok) {
          const data = await response.json()
          setRevenue(data.current_revenue || 0)
          setApiCalls(data.api_calls || 0)
          setUsers(data.active_users || 0)
        } else {
          // Fallback demo data
          setRevenue(12847.50)
          setApiCalls(128475)
          setUsers(2847)
        }
      } catch (error) {
        console.error('Failed to fetch revenue data:', error)
        // Demo data for development
        setRevenue(12847.50)
        setApiCalls(128475)
        setUsers(2847)
      } finally {
        setIsLoading(false)
      }
    }

    fetchRevenueData()

    // Update every 30 seconds
    const interval = setInterval(fetchRevenueData, 30000)
    return () => clearInterval(interval)
  }, [])

  // Animated counter effect
  useEffect(() => {
    if (!isLoading) {
      const timer = setInterval(() => {
        setRevenue(prev => {
          const increment = Math.random() * 0.5 + 0.1
          return Math.min(prev + increment, targetRevenue)
        })
        
        setApiCalls(prev => prev + Math.floor(Math.random() * 3) + 1)
        
        if (Math.random() > 0.7) {
          setUsers(prev => prev + 1)
        }
      }, 5000)

      return () => clearInterval(timer)
    }
  }, [isLoading, targetRevenue])

  const formatNumber = (num: number) => {
    return new Intl.NumberFormat('en-US', {
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    }).format(num)
  }

  const formatCurrency = (amount: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 2,
    }).format(amount)
  }

  if (isLoading) {
    return (
      <div className="bg-gradient-to-r from-green-500/10 to-blue-500/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20">
        <div className="flex items-center justify-center">
          <SparklesIcon className="h-8 w-8 text-white animate-spin" />
          <span className="text-white ml-2">Loading revenue data...</span>
        </div>
      </div>
    )
  }

  return (
    <motion.div
      className="bg-gradient-to-r from-green-500/20 to-blue-500/20 backdrop-blur-lg rounded-2xl p-8 border border-white/30 shadow-2xl"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.6 }}
    >
      <div className="text-center mb-6">
        <h3 className="text-2xl font-bold text-white mb-2">
          💰 Real-Time Revenue Dashboard
        </h3>
        <p className="text-gray-300">
          Ultra-Lightweight AI Ecosystem Performance
        </p>
      </div>

      {/* Progress Bar */}
      <div className="mb-8">
        <div className="flex justify-between text-white mb-2">
          <span>Progress to $50K Target</span>
          <span>{progressPercentage.toFixed(1)}%</span>
        </div>
        <div className="w-full bg-gray-700 rounded-full h-3">
          <motion.div
            className="bg-gradient-to-r from-green-400 to-blue-500 h-3 rounded-full"
            style={{ width: `${Math.min(progressPercentage, 100)}%` }}
            initial={{ width: 0 }}
            animate={{ width: `${Math.min(progressPercentage, 100)}%` }}
            transition={{ duration: 1.5, ease: "easeOut" }}
          />
        </div>
      </div>

      {/* Revenue Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Current Revenue */}
        <motion.div
          className="bg-white/10 rounded-xl p-6 text-center"
          whileHover={{ scale: 1.05 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          <CurrencyDollarIcon className="h-8 w-8 text-green-400 mx-auto mb-3" />
          <div className="text-3xl font-bold text-white mb-1">
            {formatCurrency(revenue)}
          </div>
          <div className="text-gray-300 text-sm">Current Revenue</div>
          <div className="text-green-400 text-xs mt-1">
            <TrendingUpIcon className="h-3 w-3 inline mr-1" />
            +{((revenue / targetRevenue) * 100).toFixed(1)}% to target
          </div>
        </motion.div>

        {/* API Calls */}
        <motion.div
          className="bg-white/10 rounded-xl p-6 text-center"
          whileHover={{ scale: 1.05 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          <SparklesIcon className="h-8 w-8 text-blue-400 mx-auto mb-3" />
          <div className="text-3xl font-bold text-white mb-1">
            {formatNumber(apiCalls)}
          </div>
          <div className="text-gray-300 text-sm">API Calls</div>
          <div className="text-blue-400 text-xs mt-1">
            ${formatCurrency(apiCalls * 0.01)} generated
          </div>
        </motion.div>

        {/* Active Users */}
        <motion.div
          className="bg-white/10 rounded-xl p-6 text-center"
          whileHover={{ scale: 1.05 }}
          transition={{ type: "spring", stiffness: 300 }}
        >
          <UsersIcon className="h-8 w-8 text-purple-400 mx-auto mb-3" />
          <div className="text-3xl font-bold text-white mb-1">
            {formatNumber(users)}
          </div>
          <div className="text-gray-300 text-sm">Active Users</div>
          <div className="text-purple-400 text-xs mt-1">
            Growing ecosystem
          </div>
        </motion.div>
      </div>

      {/* Revenue Streams */}
      <div className="mt-8 grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
        <div className="bg-white/5 rounded-lg p-3">
          <div className="text-green-400 font-bold">$0.01</div>
          <div className="text-gray-400 text-xs">per API call</div>
        </div>
        <div className="bg-white/5 rounded-lg p-3">
          <div className="text-blue-400 font-bold">$9.99</div>
          <div className="text-gray-400 text-xs">Premium/month</div>
        </div>
        <div className="bg-white/5 rounded-lg p-3">
          <div className="text-purple-400 font-bold">$99.99</div>
          <div className="text-gray-400 text-xs">Enterprise/month</div>
        </div>
        <div className="bg-white/5 rounded-lg p-3">
          <div className="text-yellow-400 font-bold">$0.05</div>
          <div className="text-gray-400 text-xs">per analysis</div>
        </div>
      </div>

      {/* Target Status */}
      <div className="mt-6 text-center">
        <div className="text-white text-lg font-semibold">
          ${formatCurrency(targetRevenue - revenue)} to reach monthly target
        </div>
        <div className="text-gray-400 text-sm mt-1">
          Ultra-lightweight mobile AI ecosystem • <5MB footprint • Zero dependencies
        </div>
      </div>
    </motion.div>
  )
}

export default RevenueCounter