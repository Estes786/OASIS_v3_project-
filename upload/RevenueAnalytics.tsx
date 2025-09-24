import React, { useState, useEffect } from 'react'
import { Line, Bar, Doughnut } from 'react-chartjs-2'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
  Filler
)

interface RevenueData {
  monthly_revenue: number[]
  revenue_streams: {
    [key: string]: number
  }
  user_growth: number[]
  api_usage: {
    labels: string[]
    data: number[]
  }
  geographic_distribution: {
    [key: string]: number
  }
}

export default function RevenueAnalytics() {
  const [revenueData, setRevenueData] = useState<RevenueData>({
    monthly_revenue: [],
    revenue_streams: {},
    user_growth: [],
    api_usage: { labels: [], data: [] },
    geographic_distribution: {}
  })

  const [timeframe, setTimeframe] = useState('12M')

  useEffect(() => {
    fetchRevenueData()
  }, [timeframe])

  const fetchRevenueData = async () => {
    try {
      const response = await fetch(`/api/revenue-analytics?timeframe=${timeframe}`)
      if (response.ok) {
        const data = await response.json()
        setRevenueData(data)
      }
    } catch (error) {
      console.error('Error fetching revenue data:', error)
    }
  }

  // Revenue trend chart configuration
  const revenueChartData = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [
      {
        label: 'Monthly Revenue ($)',
        data: revenueData.monthly_revenue,
        borderColor: '#8B5CF6',
        backgroundColor: 'rgba(139, 92, 246, 0.1)',
        borderWidth: 3,
        fill: true,
        tension: 0.4
      }
    ]
  }

  // Revenue streams breakdown
  const revenueStreamsData = {
    labels: Object.keys(revenueData.revenue_streams),
    datasets: [
      {
        data: Object.values(revenueData.revenue_streams),
        backgroundColor: [
          '#8B5CF6', // API Subscriptions
          '#10B981', // Content Generation
          '#F59E0B', // Enterprise Solutions
          '#EF4444', // Consulting Services
          '#6366F1'  // Custom AI Models
        ],
        borderWidth: 0
      }
    ]
  }

  // API usage chart
  const apiUsageData = {
    labels: revenueData.api_usage.labels,
    datasets: [
      {
        label: 'API Calls (thousands)',
        data: revenueData.api_usage.data,
        backgroundColor: 'rgba(59, 130, 246, 0.8)',
        borderColor: '#3B82F6',
        borderWidth: 1
      }
    ]
  }

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: true,
        position: 'top' as const
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        grid: {
          color: 'rgba(0, 0, 0, 0.05)'
        }
      },
      x: {
        grid: {
          color: 'rgba(0, 0, 0, 0.05)'
        }
      }
    }
  }

  return (
    <div className="space-y-6">
      {/* Header with timeframe selector */}
      <div className="flex justify-between items-center">
        <h1 className="text-3xl font-bold text-gray-900">Revenue Analytics</h1>
        <div className="flex space-x-2">
          {['1M', '3M', '6M', '12M'].map((period) => (
            <button
              key={period}
              onClick={() => setTimeframe(period)}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                timeframe === period
                  ? 'bg-purple-600 text-white'
                  : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
              }`}
            >
              {period}
            </button>
          ))}
        </div>
      </div>

      {/* Key metrics cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-gradient-to-r from-purple-500 to-pink-500 rounded-xl p-6 text-white">
          <h3 className="text-sm font-medium opacity-90">Total Revenue</h3>
          <p className="text-2xl font-bold mt-2">
            ${revenueData.monthly_revenue.reduce((a, b) => a + b, 0).toLocaleString()}
          </p>
          <p className="text-sm opacity-75 mt-1">+18.2% vs last period</p>
        </div>

        <div className="bg-gradient-to-r from-blue-500 to-cyan-500 rounded-xl p-6 text-white">
          <h3 className="text-sm font-medium opacity-90">Monthly ARR</h3>
          <p className="text-2xl font-bold mt-2">
            ${(revenueData.monthly_revenue[revenueData.monthly_revenue.length - 1] * 12).toLocaleString()}
          </p>
          <p className="text-sm opacity-75 mt-1">Annual run rate</p>
        </div>

        <div className="bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl p-6 text-white">
          <h3 className="text-sm font-medium opacity-90">API Revenue</h3>
          <p className="text-2xl font-bold mt-2">
            ${revenueData.revenue_streams['API Subscriptions']?.toLocaleString() || '0'}
          </p>
          <p className="text-sm opacity-75 mt-1">Primary revenue stream</p>
        </div>

        <div className="bg-gradient-to-r from-orange-500 to-red-500 rounded-xl p-6 text-white">
          <h3 className="text-sm font-medium opacity-90">Enterprise Revenue</h3>
          <p className="text-2xl font-bold mt-2">
            ${revenueData.revenue_streams['Enterprise Solutions']?.toLocaleString() || '0'}
          </p>
          <p className="text-sm opacity-75 mt-1">High-value contracts</p>
        </div>
      </div>

      {/* Charts grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Revenue Trend */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Revenue Trend</h2>
          <div className="h-80">
            <Line data={revenueChartData} options={chartOptions} />
          </div>
        </div>

        {/* Revenue Streams Breakdown */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Revenue Streams</h2>
          <div className="h-80">
            <Doughnut 
              data={revenueStreamsData} 
              options={{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                  legend: {
                    position: 'bottom' as const
                  }
                }
              }} 
            />
          </div>
        </div>

        {/* API Usage Analytics */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">API Usage by Service</h2>
          <div className="h-80">
            <Bar data={apiUsageData} options={chartOptions} />
          </div>
        </div>

        {/* Geographic Revenue */}
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold text-gray-900 mb-4">Revenue by Region</h2>
          <div className="space-y-4">
            {Object.entries(revenueData.geographic_distribution).map(([region, amount]) => (
              <div key={region} className="flex justify-between items-center">
                <span className="font-medium text-gray-900">{region}</span>
                <div className="flex items-center space-x-3">
                  <div className="w-32 bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-purple-600 h-2 rounded-full" 
                      style={{ 
                        width: `${(amount / Math.max(...Object.values(revenueData.geographic_distribution))) * 100}%` 
                      }}
                    />
                  </div>
                  <span className="text-sm font-semibold text-gray-700">
                    ${amount.toLocaleString()}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}