import { useState, useEffect } from 'react'
import Head from 'next/head'
import { motion } from 'framer-motion'
import { 
  RocketLaunchIcon, 
  DevicePhoneMobileIcon, 
  CloudIcon, 
  CurrencyDollarIcon,
  ChartBarIcon,
  SparklesIcon,
  BoltIcon,
  GlobeAltIcon,
  CpuChipIcon,
  MegaphoneIcon
} from '@heroicons/react/24/outline'
import Layout from '../components/Layout'
import AIProcessingDemo from '../components/AIProcessingDemo'
import RevenueCounter from '../components/RevenueCounter'
import FeatureCard from '../components/FeatureCard'
import TechStack from '../components/TechStack'

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      delayChildren: 0.3,
      staggerChildren: 0.2
    }
  }
}

const itemVariants = {
  hidden: { y: 20, opacity: 0 },
  visible: {
    y: 0,
    opacity: 1
  }
}

export default function Home() {
  const [isLoaded, setIsLoaded] = useState(false)

  useEffect(() => {
    setIsLoaded(true)
  }, [])

  const features = [
    {
      icon: <DevicePhoneMobileIcon className="h-8 w-8" />,
      title: "Ultra-Lightweight",
      description: "< 5MB footprint vs 500MB+ traditional ML setups",
      gradient: "from-blue-500 to-cyan-500"
    },
    {
      icon: <CloudIcon className="h-8 w-8" />,
      title: "Cloud-First AI",
      description: "100% HuggingFace API processing, zero local dependencies",
      gradient: "from-purple-500 to-pink-500"
    },
    {
      icon: <BoltIcon className="h-8 w-8" />,
      title: "Zero Dependencies",
      description: "Python + urllib only, eliminating dependency hell",
      gradient: "from-yellow-500 to-orange-500"
    },
    {
      icon: <CurrencyDollarIcon className="h-8 w-8" />,
      title: "$50K+/Month Target",
      description: "Multiple revenue streams: API, Premium, Enterprise",
      gradient: "from-green-500 to-emerald-500"
    },
    {
      icon: <RocketLaunchIcon className="h-8 w-8" />,
      title: "Production Ready",
      description: "Deployed on HuggingFace Spaces, Vercel, Supabase",
      gradient: "from-red-500 to-rose-500"
    },
    {
      icon: <GlobeAltIcon className="h-8 w-8" />,
      title: "Global Scale",
      description: "Multi-modal AI: Text, Sentiment, Translation, Q&A",
      gradient: "from-indigo-500 to-blue-500"
    }
  ]

  return (
    <Layout>
      <Head>
        <title>OASIS v3 - AI Superintelligence Ecosystem</title>
        <meta name="description" content="Ultra-Lightweight Mobile AI Architecture targeting $50K+/month revenue. Zero dependencies, cloud-first, API-driven superintelligence ecosystem." />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 overflow-hidden">
        {/* Animated background */}
        <div className="absolute inset-0 overflow-hidden">
          <div className="absolute -inset-10 opacity-20">
            {[...Array(50)].map((_, i) => (
              <motion.div
                key={i}
                className="absolute bg-white rounded-full"
                style={{
                  left: `${Math.random() * 100}%`,
                  top: `${Math.random() * 100}%`,
                  width: `${Math.random() * 4 + 1}px`,
                  height: `${Math.random() * 4 + 1}px`,
                }}
                animate={{
                  y: [-20, 20],
                  opacity: [0.5, 1, 0.5],
                }}
                transition={{
                  duration: Math.random() * 3 + 2,
                  repeat: Infinity,
                  ease: "easeInOut",
                }}
              />
            ))}
          </div>
        </div>

        <motion.div
          className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center"
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          <motion.div variants={itemVariants} className="mb-8">
            <SparklesIcon className="h-16 w-16 text-yellow-400 mx-auto mb-4 animate-pulse" />
            <h1 className="text-6xl md:text-8xl font-extrabold text-white mb-6">
              <span className="bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 bg-clip-text text-transparent">
                OASIS v3
              </span>
            </h1>
            <p className="text-2xl md:text-3xl text-gray-300 font-semibold mb-4">
              AI Superintelligence Ecosystem
            </p>
            <p className="text-lg md:text-xl text-gray-400 max-w-3xl mx-auto">
              Ultra-Lightweight Mobile Architecture • Zero Dependencies • Cloud-First • $50K+/Month Revenue Target
            </p>
          </motion.div>

          <motion.div variants={itemVariants} className="mb-12">
            <div className="flex flex-wrap justify-center gap-4 text-sm md:text-base">
              <div className="bg-green-500/20 text-green-300 px-4 py-2 rounded-full border border-green-500/30">
                <BoltIcon className="h-4 w-4 inline mr-2" />
                &lt; 5MB Footprint
              </div>
              <div className="bg-blue-500/20 text-blue-300 px-4 py-2 rounded-full border border-blue-500/30">
                <CloudIcon className="h-4 w-4 inline mr-2" />
                100% Cloud Processing
              </div>
              <div className="bg-purple-500/20 text-purple-300 px-4 py-2 rounded-full border border-purple-500/30">
                <CpuChipIcon className="h-4 w-4 inline mr-2" />
                Production Ready
              </div>
              <div className="bg-yellow-500/20 text-yellow-300 px-4 py-2 rounded-full border border-yellow-500/30">
                <CurrencyDollarIcon className="h-4 w-4 inline mr-2" />
                Revenue Optimized
              </div>
            </div>
          </motion.div>

          <motion.div variants={itemVariants} className="flex flex-col sm:flex-row justify-center gap-4">
            <button className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105 shadow-2xl">
              <RocketLaunchIcon className="h-6 w-6 inline mr-2" />
              Launch Demo
            </button>
            <button className="bg-white/10 hover:bg-white/20 text-white border border-white/30 px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 backdrop-blur-sm">
              <ChartBarIcon className="h-6 w-6 inline mr-2" />
              Revenue Dashboard
            </button>
          </motion.div>

          <motion.div variants={itemVariants} className="mt-16">
            <RevenueCounter />
          </motion.div>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-gray-50 dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
              Revolutionary Architecture
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto">
              Solving the dependency nightmare with ultra-lightweight mobile AI orchestration
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1, duration: 0.6 }}
              >
                <FeatureCard {...feature} />
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* AI Processing Demo */}
      <section className="py-20 bg-white dark:bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
              Live AI Processing
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto">
              Experience the power of cloud-first AI superintelligence
            </p>
          </motion.div>

          <AIProcessingDemo />
        </div>
      </section>

      {/* Tech Stack */}
      <section className="py-20 bg-gray-50 dark:bg-gray-900">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <h2 className="text-4xl md:text-5xl font-bold text-gray-900 dark:text-white mb-4">
              Production Stack
            </h2>
            <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto">
              Built with cutting-edge technologies for maximum performance and scalability
            </p>
          </motion.div>

          <TechStack />
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-purple-700">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6 }}
          >
            <MegaphoneIcon className="h-16 w-16 text-white mx-auto mb-6" />
            <h2 className="text-4xl md:text-5xl font-bold text-white mb-6">
              Ready for $50K+/Month?
            </h2>
            <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
              Join the AI superintelligence revolution. Deploy your ultra-lightweight mobile AI ecosystem today.
            </p>
            <div className="flex flex-col sm:flex-row justify-center gap-4">
              <button className="bg-white hover:bg-gray-100 text-blue-600 px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 transform hover:scale-105">
                Start Building
              </button>
              <button className="bg-white/20 hover:bg-white/30 text-white border border-white/30 px-8 py-4 rounded-xl font-semibold text-lg transition-all duration-300 backdrop-blur-sm">
                View Documentation
              </button>
            </div>
          </motion.div>
        </div>
      </section>
    </Layout>
  )
}