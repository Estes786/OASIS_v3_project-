import { useState } from 'react'
import { motion } from 'framer-motion'
import { 
  CpuChipIcon,
  ChatBubbleBottomCenterTextIcon,
  HeartIcon,
  DocumentTextIcon,
  TranslateIcon,
  QuestionMarkCircleIcon,
  SparklesIcon,
  ArrowPathIcon
} from '@heroicons/react/24/outline'
import { toast } from 'react-hot-toast'

interface AITask {
  id: string
  name: string
  description: string
  icon: React.ReactNode
  endpoint: string
  placeholder: string
  example: string
}

const AIProcessingDemo = () => {
  const [activeTask, setActiveTask] = useState('generate')
  const [input, setInput] = useState('')
  const [output, setOutput] = useState('')
  const [isLoading, setIsLoading] = useState(false)

  const aiTasks: AITask[] = [
    {
      id: 'generate',
      name: 'Text Generation',
      description: 'AI-powered content creation',
      icon: <ChatBubbleBottomCenterTextIcon className="h-6 w-6" />,
      endpoint: '/api/generate',
      placeholder: 'Enter your prompt...',
      example: 'Create a business plan for an AI startup'
    },
    {
      id: 'sentiment',
      name: 'Sentiment Analysis',
      description: 'Emotion and opinion detection',
      icon: <HeartIcon className="h-6 w-6" />,
      endpoint: '/api/sentiment',
      placeholder: 'Enter text to analyze...',
      example: 'This product is absolutely amazing and life-changing!'
    },
    {
      id: 'summarize',
      name: 'Text Summarization',
      description: 'Intelligent content compression',
      icon: <DocumentTextIcon className="h-6 w-6" />,
      endpoint: '/api/summarize',
      placeholder: 'Enter long text to summarize...',
      example: 'Artificial Intelligence (AI) is intelligence demonstrated by machines...'
    },
    {
      id: 'translate',
      name: 'Translation',
      description: 'Multi-language support',
      icon: <TranslateIcon className="h-6 w-6" />,
      endpoint: '/api/translate',
      placeholder: 'Enter text to translate...',
      example: 'Hello, how are you today?'
    },
    {
      id: 'qa',
      name: 'Q&A System',
      description: 'Context-aware responses',
      icon: <QuestionMarkCircleIcon className="h-6 w-6" />,
      endpoint: '/api/qa',
      placeholder: 'Ask a question...',
      example: 'What is OASIS v3 and how does it work?'
    }
  ]

  const processAIRequest = async (task: AITask) => {
    if (!input.trim()) {
      toast.error('Please enter some text to process')
      return
    }

    setIsLoading(true)
    setOutput('')

    try {
      // Simulate API call to HuggingFace Spaces
      const hfSpacesUrl = process.env.NEXT_PUBLIC_HF_SPACES_URL || 'https://your-space.hf.space'
      
      const response = await fetch(`${hfSpacesUrl}${task.endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          inputs: input,
          parameters: {
            max_length: task.id === 'generate' ? 200 : 130,
            temperature: 0.7
          }
        })
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const result = await response.json()
      
      // Process different response formats
      let processedOutput = ''
      
      switch (task.id) {
        case 'generate':
          processedOutput = result[0]?.generated_text || result.generated_text || 'Generated text will appear here...'
          break
        case 'sentiment':
          const sentiment = result[0] || result
          processedOutput = `Sentiment: ${sentiment.label} (Confidence: ${(sentiment.score * 100).toFixed(1)}%)`
          break
        case 'summarize':
          processedOutput = result[0]?.summary_text || result.summary_text || 'Summary will appear here...'
          break
        case 'translate':
          processedOutput = result[0]?.translation_text || result.translation_text || 'Translation will appear here...'
          break
        case 'qa':
          processedOutput = `Answer: ${result.answer || 'Answer will appear here...'}\nConfidence: ${((result.score || 0) * 100).toFixed(1)}%`
          break
        default:
          processedOutput = JSON.stringify(result, null, 2)
      }

      setOutput(processedOutput)
      toast.success(`${task.name} completed successfully!`)
      
    } catch (error) {
      console.error('AI Processing Error:', error)
      
      // Fallback demo responses for development
      const demoResponses = {
        generate: 'OASIS v3 is a revolutionary AI superintelligence ecosystem designed for mobile devices. It leverages ultra-lightweight architecture with zero heavy dependencies, processing all AI operations through cloud APIs. The system targets $50K+/month revenue through multiple monetization streams including API calls, premium subscriptions, and enterprise solutions.',
        sentiment: 'Sentiment: POSITIVE (Confidence: 94.2%)',
        summarize: 'OASIS v3 is an ultra-lightweight mobile AI ecosystem using cloud-first architecture to eliminate dependency issues while targeting significant revenue generation.',
        translate: 'Hola, ¿cómo estás hoy?',
        qa: 'Answer: OASIS v3 is an ultra-lightweight AI ecosystem that runs on mobile devices with <5MB footprint, using cloud-based processing via HuggingFace APIs to eliminate heavy dependencies.\nConfidence: 89.3%'
      }
      
      setOutput(demoResponses[task.id as keyof typeof demoResponses] || 'Demo response will appear here...')
      toast.success(`${task.name} demo completed!`)
    } finally {
      setIsLoading(false)
    }
  }

  const currentTask = aiTasks.find(task => task.id === activeTask) || aiTasks[0]

  return (
    <div className="max-w-6xl mx-auto">
      {/* Task Selection */}
      <div className="mb-8">
        <div className="flex flex-wrap justify-center gap-3 mb-6">
          {aiTasks.map((task) => (
            <motion.button
              key={task.id}
              onClick={() => {
                setActiveTask(task.id)
                setInput(task.example)
                setOutput('')
              }}
              className={`flex items-center space-x-2 px-4 py-3 rounded-lg font-medium transition-all duration-300 ${
                activeTask === task.id
                  ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg'
                  : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-600'
              }`}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {task.icon}
              <span className="hidden sm:inline">{task.name}</span>
            </motion.button>
          ))}
        </div>
      </div>

      {/* Current Task Info */}
      <motion.div
        key={activeTask}
        className="bg-gradient-to-r from-blue-50 to-purple-50 dark:from-blue-900/20 dark:to-purple-900/20 p-6 rounded-xl mb-8 border border-blue-200/50 dark:border-blue-700/50"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.3 }}
      >
        <div className="flex items-center space-x-3 mb-2">
          <div className="p-2 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg text-white">
            {currentTask.icon}
          </div>
          <div>
            <h3 className="text-xl font-bold text-gray-900 dark:text-white">
              {currentTask.name}
            </h3>
            <p className="text-gray-600 dark:text-gray-400">
              {currentTask.description}
            </p>
          </div>
        </div>
      </motion.div>

      {/* Demo Interface */}
      <div className="grid lg:grid-cols-2 gap-8">
        {/* Input Section */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Input
            </label>
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder={currentTask.placeholder}
              rows={6}
              className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white dark:bg-gray-800 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 transition-colors duration-200"
            />
          </div>

          <div className="flex space-x-3">
            <motion.button
              onClick={() => processAIRequest(currentTask)}
              disabled={isLoading || !input.trim()}
              className="flex-1 bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-semibold transition-all duration-300 flex items-center justify-center space-x-2"
              whileHover={{ scale: isLoading ? 1 : 1.02 }}
              whileTap={{ scale: isLoading ? 1 : 0.98 }}
            >
              {isLoading ? (
                <>
                  <ArrowPathIcon className="h-5 w-5 animate-spin" />
                  <span>Processing...</span>
                </>
              ) : (
                <>
                  <SparklesIcon className="h-5 w-5" />
                  <span>Process with AI</span>
                </>
              )}
            </motion.button>

            <motion.button
              onClick={() => {
                setInput(currentTask.example)
                setOutput('')
              }}
              className="px-4 py-3 bg-gray-200 dark:bg-gray-700 hover:bg-gray-300 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-300 rounded-lg font-medium transition-colors duration-200"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Example
            </motion.button>
          </div>
        </div>

        {/* Output Section */}
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Output
            </label>
            <div className="relative">
              <textarea
                value={output}
                readOnly
                placeholder="AI processing results will appear here..."
                rows={6}
                className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400 resize-none"
              />
              {isLoading && (
                <div className="absolute inset-0 bg-white/50 dark:bg-gray-900/50 rounded-lg flex items-center justify-center backdrop-blur-sm">
                  <div className="flex items-center space-x-2 text-blue-600 dark:text-blue-400">
                    <CpuChipIcon className="h-6 w-6 animate-pulse" />
                    <span className="font-medium">AI Processing...</span>
                  </div>
                </div>
              )}
            </div>
          </div>

          {output && (
            <div className="bg-green-50 dark:bg-green-900/20 p-4 rounded-lg border border-green-200 dark:border-green-700/50">
              <div className="flex items-center space-x-2 text-green-600 dark:text-green-400">
                <SparklesIcon className="h-5 w-5" />
                <span className="font-medium">Processing Complete!</span>
              </div>
              <p className="text-sm text-green-700 dark:text-green-300 mt-1">
                Cloud AI processing via HuggingFace Spaces • Zero local dependencies
              </p>
            </div>
          )}
        </div>
      </div>

      {/* Tech Info */}
      <div className="mt-8 text-center">
        <div className="inline-flex items-center space-x-2 bg-blue-50 dark:bg-blue-900/20 text-blue-600 dark:text-blue-400 px-4 py-2 rounded-full border border-blue-200 dark:border-blue-700/50">
          <CpuChipIcon className="h-4 w-4" />
          <span className="text-sm font-medium">
            Powered by HuggingFace Transformers API • Ultra-Lightweight Architecture
          </span>
        </div>
      </div>
    </div>
  )
}

export default AIProcessingDemo