import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  RocketLaunchIcon, 
  Bars3Icon, 
  XMarkIcon,
  CurrencyDollarIcon,
  ChartBarIcon,
  DocumentTextIcon,
  DevicePhoneMobileIcon
} from '@heroicons/react/24/outline'

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const navigation = [
    { name: 'Demo', href: '#demo', icon: <RocketLaunchIcon className="h-4 w-4" /> },
    { name: 'Revenue', href: '#revenue', icon: <CurrencyDollarIcon className="h-4 w-4" /> },
    { name: 'Analytics', href: '#analytics', icon: <ChartBarIcon className="h-4 w-4" /> },
    { name: 'Termux', href: '#termux', icon: <DevicePhoneMobileIcon className="h-4 w-4" /> },
    { name: 'Docs', href: '#docs', icon: <DocumentTextIcon className="h-4 w-4" /> },
  ]

  return (
    <header className="fixed top-0 left-0 right-0 z-50 bg-white/80 dark:bg-gray-900/80 backdrop-blur-lg border-b border-gray-200/20 dark:border-gray-700/20">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <motion.div 
            className="flex items-center space-x-2"
            whileHover={{ scale: 1.05 }}
            transition={{ type: "spring", stiffness: 400, damping: 10 }}
          >
            <div className="h-8 w-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
              <RocketLaunchIcon className="h-5 w-5 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
                OASIS v3
              </h1>
              <p className="text-xs text-gray-500 dark:text-gray-400 -mt-1">
                AI Superintelligence
              </p>
            </div>
          </motion.div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center space-x-8">
            {navigation.map((item) => (
              <motion.a
                key={item.name}
                href={item.href}
                className="flex items-center space-x-1 text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-200 font-medium"
                whileHover={{ y: -1 }}
                transition={{ type: "spring", stiffness: 400, damping: 10 }}
              >
                {item.icon}
                <span>{item.name}</span>
              </motion.a>
            ))}
          </div>

          {/* Revenue Display */}
          <div className="hidden md:flex items-center space-x-4">
            <div className="flex items-center space-x-2 bg-green-500/10 text-green-600 dark:text-green-400 px-3 py-1 rounded-full border border-green-500/20">
              <CurrencyDollarIcon className="h-4 w-4" />
              <span className="text-sm font-semibold">$50K Target</span>
            </div>
            
            <motion.button
              className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white px-4 py-2 rounded-lg font-medium transition-all duration-300 text-sm"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Launch Demo
            </motion.button>
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <motion.button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white"
              whileTap={{ scale: 0.95 }}
            >
              {isMenuOpen ? (
                <XMarkIcon className="h-6 w-6" />
              ) : (
                <Bars3Icon className="h-6 w-6" />
              )}
            </motion.button>
          </div>
        </div>
      </nav>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <motion.div
          className="md:hidden bg-white dark:bg-gray-900 border-t border-gray-200 dark:border-gray-700"
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.2 }}
        >
          <div className="px-4 py-4 space-y-3">
            {navigation.map((item) => (
              <motion.a
                key={item.name}
                href={item.href}
                className="flex items-center space-x-2 text-gray-600 dark:text-gray-300 hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-200 font-medium py-2"
                onClick={() => setIsMenuOpen(false)}
                whileHover={{ x: 5 }}
                transition={{ type: "spring", stiffness: 400, damping: 10 }}
              >
                {item.icon}
                <span>{item.name}</span>
              </motion.a>
            ))}
            
            <div className="pt-4 border-t border-gray-200 dark:border-gray-700">
              <div className="flex items-center space-x-2 bg-green-500/10 text-green-600 dark:text-green-400 px-3 py-2 rounded-lg border border-green-500/20 mb-3">
                <CurrencyDollarIcon className="h-4 w-4" />
                <span className="text-sm font-semibold">$50K Target</span>
              </div>
              
              <motion.button
                className="w-full bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white px-4 py-2 rounded-lg font-medium transition-all duration-300 text-sm"
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                Launch Demo
              </motion.button>
            </div>
          </div>
        </motion.div>
      )}
    </header>
  )
}

export default Header