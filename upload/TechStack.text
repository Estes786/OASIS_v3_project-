import { motion } from 'framer-motion'

const TechStack = () => {
  const technologies = [
    {
      category: "Frontend",
      color: "from-blue-500 to-cyan-500",
      techs: [
        { name: "Next.js 14", icon: "⚡", description: "React framework with SSG" },
        { name: "TypeScript", icon: "🔷", description: "Type-safe development" },
        { name: "Tailwind CSS", icon: "🎨", description: "Utility-first styling" },
        { name: "Framer Motion", icon: "🌊", description: "Smooth animations" }
      ]
    },
    {
      category: "Backend",
      color: "from-purple-500 to-pink-500", 
      techs: [
        { name: "HuggingFace Spaces", icon: "🤗", description: "AI model hosting" },
        { name: "Gradio", icon: "🚀", description: "ML app framework" },
        { name: "Python 3.9+", icon: "🐍", description: "Backend processing" },
        { name: "Transformers API", icon: "🧠", description: "AI capabilities" }
      ]
    },
    {
      category: "Mobile",
      color: "from-green-500 to-emerald-500",
      techs: [
        { name: "Termux", icon: "📱", description: "Android terminal" },
        { name: "Python stdlib", icon: "⚡", description: "Zero dependencies" },
        { name: "urllib", icon: "🌐", description: "HTTP requests only" },
        { name: "<5MB footprint", icon: "🪶", description: "Ultra-lightweight" }
      ]
    },
    {
      category: "Infrastructure",
      color: "from-orange-500 to-red-500",
      techs: [
        { name: "Vercel", icon: "▲", description: "Edge deployment" },
        { name: "Supabase", icon: "🗄️", description: "PostgreSQL backend" },
        { name: "GitHub Actions", icon: "🔄", description: "CI/CD automation" },
        { name: "Edge Functions", icon: "⚡", description: "Serverless compute" }
      ]
    }
  ]

  return (
    <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
      {technologies.map((category, categoryIndex) => (
        <motion.div
          key={category.category}
          className="space-y-6"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ delay: categoryIndex * 0.1, duration: 0.6 }}
        >
          {/* Category Header */}
          <div className="text-center">
            <div className={`inline-flex items-center justify-center w-12 h-12 rounded-xl bg-gradient-to-r ${category.color} text-white font-bold text-lg mb-3`}>
              {category.category.charAt(0)}
            </div>
            <h3 className="text-xl font-bold text-gray-900 dark:text-white">
              {category.category}
            </h3>
          </div>

          {/* Technologies */}
          <div className="space-y-4">
            {category.techs.map((tech, techIndex) => (
              <motion.div
                key={tech.name}
                className="bg-white dark:bg-gray-800 rounded-lg p-4 border border-gray-200 dark:border-gray-700 hover:shadow-lg transition-all duration-300 group"
                whileHover={{ scale: 1.02 }}
                transition={{ type: "spring", stiffness: 300, damping: 30 }}
              >
                <div className="flex items-center space-x-3 mb-2">
                  <span className="text-2xl group-hover:scale-110 transition-transform duration-300">
                    {tech.icon}
                  </span>
                  <div>
                    <h4 className="font-semibold text-gray-900 dark:text-white text-sm">
                      {tech.name}
                    </h4>
                  </div>
                </div>
                <p className="text-xs text-gray-600 dark:text-gray-400 group-hover:text-gray-700 dark:group-hover:text-gray-300 transition-colors duration-300">
                  {tech.description}
                </p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      ))}
    </div>
  )
}

export default TechStack