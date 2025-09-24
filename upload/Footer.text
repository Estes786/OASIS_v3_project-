import { motion } from 'framer-motion'
import { 
  RocketLaunchIcon,
  HeartIcon,
  CurrencyDollarIcon,
  DevicePhoneMobileIcon,
  CloudIcon,
  BoltIcon
} from '@heroicons/react/24/outline'

const Footer = () => {
  const currentYear = new Date().getFullYear()

  const links = {
    product: [
      { name: 'AI Processing', href: '#ai-processing' },
      { name: 'Revenue Dashboard', href: '#revenue' },
      { name: 'Termux Setup', href: '#termux' },
      { name: 'API Documentation', href: '#docs' }
    ],
    resources: [
      { name: 'Deployment Guide', href: '/DEPLOYMENT_GUIDE.md' },
      { name: 'Quickstart', href: '/QUICKSTART.md' },
      { name: 'GitHub Repository', href: 'https://github.com/your-username/oasis-v3' },
      { name: 'HuggingFace Space', href: 'https://huggingface.co/spaces/your-username/oasis-v3' }
    ],
    company: [
      { name: 'About OASIS v3', href: '#about' },
      { name: 'Revenue Model', href: '#revenue-model' },
      { name: 'Architecture', href: '#architecture' },
      { name: 'Contact', href: '#contact' }
    ]
  }

  const stats = [
    { icon: <DevicePhoneMobileIcon className="h-5 w-5" />, label: 'Mobile Footprint', value: '<5MB' },
    { icon: <BoltIcon className="h-5 w-5" />, label: 'Dependencies', value: 'Zero' },
    { icon: <CloudIcon className="h-5 w-5" />, label: 'AI Processing', value: '100% Cloud' },
    { icon: <CurrencyDollarIcon className="h-5 w-5" />, label: 'Revenue Target', value: '$50K/mo' }
  ]

  return (
    <footer className="bg-gray-900 text-white">
      {/* Stats Section */}
      <div className="border-b border-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            {stats.map((stat, index) => (
              <motion.div
                key={stat.label}
                className="space-y-2"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1, duration: 0.6 }}
              >
                <div className="flex justify-center text-blue-400">
                  {stat.icon}
                </div>
                <div className="text-2xl font-bold text-white">{stat.value}</div>
                <div className="text-sm text-gray-400">{stat.label}</div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>

      {/* Main Footer Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          
          {/* Brand Section */}
          <div className="lg:col-span-1">
            <motion.div 
              className="flex items-center space-x-2 mb-4"
              whileHover={{ scale: 1.05 }}
              transition={{ type: "spring", stiffness: 400, damping: 10 }}
            >
              <div className="h-10 w-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
                <RocketLaunchIcon className="h-6 w-6 text-white" />
              </div>
              <div>
                <h2 className="text-xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">
                  OASIS v3
                </h2>
                <p className="text-xs text-gray-400">AI Superintelligence</p>
              </div>
            </motion.div>
            
            <p className="text-gray-400 text-sm mb-4">
              Ultra-Lightweight Mobile AI Superintelligence Ecosystem targeting $50K+/month revenue with zero dependencies and cloud-first architecture.
            </p>
            
            <div className="flex space-x-2">
              <div className="bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-xs border border-green-500/30">
                Production Ready
              </div>
              <div className="bg-blue-500/20 text-blue-400 px-3 py-1 rounded-full text-xs border border-blue-500/30">
                Open Source
              </div>
            </div>
          </div>

          {/* Product Links */}
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">Product</h3>
            <ul className="space-y-3">
              {links.product.map((link) => (
                <li key={link.name}>
                  <a 
                    href={link.href}
                    className="text-gray-400 hover:text-white transition-colors duration-200 text-sm"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Resources Links */}
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">Resources</h3>
            <ul className="space-y-3">
              {links.resources.map((link) => (
                <li key={link.name}>
                  <a 
                    href={link.href}
                    target={link.href.startsWith('http') ? '_blank' : undefined}
                    rel={link.href.startsWith('http') ? 'noopener noreferrer' : undefined}
                    className="text-gray-400 hover:text-white transition-colors duration-200 text-sm"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Company Links */}
          <div>
            <h3 className="text-lg font-semibold text-white mb-4">Company</h3>
            <ul className="space-y-3">
              {links.company.map((link) => (
                <li key={link.name}>
                  <a 
                    href={link.href}
                    className="text-gray-400 hover:text-white transition-colors duration-200 text-sm"
                  >
                    {link.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center space-y-4 md:space-y-0">
            
            {/* Copyright */}
            <div className="text-gray-400 text-sm">
              © {currentYear} OASIS v3. Open Source AI Superintelligence Ecosystem.
            </div>

            {/* Key Features */}
            <div className="flex items-center space-x-6 text-xs">
              <div className="flex items-center space-x-1 text-gray-400">
                <DevicePhoneMobileIcon className="h-3 w-3" />
                <span>&lt;5MB Footprint</span>
              </div>
              <div className="flex items-center space-x-1 text-gray-400">
                <BoltIcon className="h-3 w-3" />
                <span>Zero Dependencies</span>
              </div>
              <div className="flex items-center space-x-1 text-gray-400">
                <CurrencyDollarIcon className="h-3 w-3" />
                <span>$50K Target</span>
              </div>
            </div>

            {/* Made with Love */}
            <div className="flex items-center space-x-1 text-gray-400 text-sm">
              <span>Made with</span>
              <HeartIcon className="h-4 w-4 text-red-500" />
              <span>for the AI revolution</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}

export default Footer