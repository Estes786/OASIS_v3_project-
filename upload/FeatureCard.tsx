import { motion } from 'framer-motion'
import { ReactNode } from 'react'

interface FeatureCardProps {
  icon: ReactNode
  title: string
  description: string
  gradient: string
}

const FeatureCard = ({ icon, title, description, gradient }: FeatureCardProps) => {
  return (
    <motion.div
      className="relative group"
      whileHover={{ y: -5 }}
      transition={{ type: "spring", stiffness: 300, damping: 30 }}
    >
      <div className="absolute inset-0 bg-gradient-to-r opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-2xl blur-xl"
           style={{
             background: `linear-gradient(135deg, var(--tw-gradient-stops))`,
             backgroundImage: `linear-gradient(135deg, ${gradient.replace('from-', '').replace('to-', ', ')})`
           }} 
      />
      
      <div className="relative bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-xl border border-gray-200 dark:border-gray-700 transition-all duration-300 group-hover:shadow-2xl group-hover:border-transparent">
        {/* Icon */}
        <div className={`inline-flex items-center justify-center w-16 h-16 rounded-xl bg-gradient-to-r ${gradient} text-white mb-6 group-hover:scale-110 transition-transform duration-300`}>
          {icon}
        </div>
        
        {/* Content */}
        <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3 group-hover:text-transparent group-hover:bg-clip-text group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 transition-all duration-300">
          {title}
        </h3>
        
        <p className="text-gray-600 dark:text-gray-400 leading-relaxed group-hover:text-gray-700 dark:group-hover:text-gray-300 transition-colors duration-300">
          {description}
        </p>
        
        {/* Decorative elements */}
        <div className="absolute top-4 right-4 w-2 h-2 bg-gradient-to-r opacity-20 rounded-full group-hover:opacity-60 transition-opacity duration-300"
             style={{
               background: `linear-gradient(135deg, ${gradient.replace('from-', '').replace('to-', ', ')})`
             }}
        />
        
        <div className="absolute bottom-4 left-4 w-1 h-1 bg-gradient-to-r opacity-10 rounded-full group-hover:opacity-40 transition-opacity duration-300"
             style={{
               background: `linear-gradient(135deg, ${gradient.replace('from-', '').replace('to-', ', ')})`
             }}
        />
      </div>
    </motion.div>
  )
}

export default FeatureCard