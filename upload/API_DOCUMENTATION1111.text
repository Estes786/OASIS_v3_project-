# 📖 **THE NEW CIVILIZATION - API DOCUMENTATION**

Complete API reference for ultra-lightweight AI platform with mobile orchestration.

---

## 🚀 **Base Configuration**

### **Endpoints**
- **Production**: `https://elmatador0197-my-oasis-agent.hf.space`
- **Local Development**: `http://localhost:7860`
- **API Version**: `3.0.0`

### **Authentication**
- **HF Token**: `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`
- **Session-based**: Create session for tracking
- **Rate Limiting**: Based on subscription tier

### **Response Format**
All API responses follow consistent JSON structure:
```json
{
  "status": "success",
  "data": {...},
  "timestamp": "2024-01-15T10:30:00Z",
  "cost": 0.05,
  "model_used": "microsoft/DialoGPT-medium"
}
```

---

## 🔤 **TEXT GENERATION SERVICES**

### **1. Generate Text**
Advanced text generation using HuggingFace models.

```http
POST /api/text/generate
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "Write a story about artificial intelligence",
  "model": "microsoft/DialoGPT-medium",
  "max_length": 100,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "generated_text": "Write a story about artificial intelligence that changes the world...",
  "model_used": "microsoft/DialoGPT-medium", 
  "timestamp": "2024-01-15T10:30:00Z",
  "cost": 0.05
}
```

**Supported Models:**
- `microsoft/DialoGPT-medium` (default)
- `microsoft/DialoGPT-large`
- `facebook/blenderbot-400M-distill`

### **2. Chat Completion**
Interactive conversational AI for natural dialogue.

```http  
POST /api/text/chat
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "What is the meaning of life?",
  "model": "microsoft/DialoGPT-medium",
  "max_length": 80,
  "temperature": 0.8
}
```

**Response:**
```json
{
  "response": "The meaning of life is to find purpose and happiness...",
  "model_used": "microsoft/DialoGPT-medium",
  "timestamp": "2024-01-15T10:30:00Z", 
  "conversation_id": "conv_12345"
}
```

---

## 🎨 **IMAGE GENERATION SERVICES**

### **Generate Images**
Create images from text prompts using AI models.

```http
POST /api/image/generate  
Content-Type: application/json
```

**Request Body:**
```json
{
  "prompt": "A futuristic city with flying cars at sunset",
  "model": "runwayml/stable-diffusion-v1-5",
  "width": 512,
  "height": 512
}
```

**Response:**
```json
{
  "image_data": "base64_encoded_image_data",
  "prompt": "A futuristic city with flying cars at sunset",
  "model_used": "runwayml/stable-diffusion-v1-5",
  "timestamp": "2024-01-15T10:30:00Z",
  "cost": 0.10
}
```

**Supported Models:**
- `runwayml/stable-diffusion-v1-5` (default)
- `CompVis/stable-diffusion-v1-4`

---

## 🌍 **TRANSLATION SERVICES**

### **Translate Text**
Multi-language translation with automatic model selection.

```http
POST /api/translate
Content-Type: application/json  
```

**Request Body:**
```json
{
  "text": "Hello, how are you today?",
  "source_lang": "en",
  "target_lang": "id"
}
```

**Response:**
```json
{
  "translated_text": "Halo, apa kabar hari ini?",
  "source_language": "en",
  "target_language": "id", 
  "model_used": "Helsinki-NLP/opus-mt-en-id",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**Supported Language Pairs:**
- English ↔ Indonesian (`en-id`, `id-en`)
- English → Spanish (`en-es`)  
- English → French (`en-fr`)
- English → German (`en-de`)

---

## 🧠 **TEXT ANALYSIS SERVICES**

### **Analyze Text**
Sentiment analysis, emotion detection, and content classification.

```http
POST /api/analyze
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "I love this new AI platform! It's amazing!",
  "analysis_type": "sentiment"
}
```

**Response:**
```json
{
  "analysis_result": [
    {
      "label": "POSITIVE",
      "score": 0.9998
    }
  ],
  "analysis_type": "sentiment",
  "text_analyzed": "I love this new AI platform! It's amazing!",
  "model_used": "cardiffnlp/twitter-roberta-base-sentiment-latest",
  "timestamp": "2024-01-15T10:30:00Z",
  "confidence_score": 0.9998
}
```

**Analysis Types:**
- `sentiment` - Positive/Negative/Neutral sentiment  
- `emotion` - Joy, anger, sadness, fear, etc.
- `classification` - Content categorization
- `toxicity` - Toxic content detection

---

## 📱 **TERMUX INTEGRATION**

### **1. Termux Status**
Check mobile orchestrator status and configuration.

```http
GET /api/termux/status
```

**Response:**
```json
{
  "status": "online",
  "architecture": "ultra-lightweight", 
  "dependencies": ["python", "urllib"],
  "memory_footprint": "<5MB",
  "connection": "api-first",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### **2. Execute Command**
Execute commands through Termux orchestrator.

```http
POST /api/termux/execute
Content-Type: application/json
```

**Request Body:**
```json
{
  "cmd": "generate_text",
  "params": {
    "text": "Hello AI",
    "model": "microsoft/DialoGPT-medium"
  }
}
```

**Response:**
```json
{
  "command_id": "cmd_12345",
  "status": "executed", 
  "result": "Command 'generate_text' processed via API",
  "execution_time": "0.01s",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

---

## 💰 **REVENUE & ANALYTICS**

### **1. Revenue Statistics**
Real-time revenue and usage statistics.

```http
GET /api/revenue/stats
```

**Response:**
```json
{
  "total_revenue": 156.78,
  "total_requests": 3142,
  "active_users": 87,
  "average_request_cost": 0.05,
  "projected_monthly": 4703.40,
  "status": "profitable",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### **2. Revenue Dashboard** 
Comprehensive business analytics and metrics.

```http
GET /api/revenue/dashboard
```

**Response:**
```json
{
  "current_revenue": 156.78,
  "target_revenue": 1000.0,
  "progress_percentage": 15.68,
  "services_breakdown": {
    "text_generation": 1256,
    "image_generation": 628,
    "translation": 628, 
    "analysis": 628
  },
  "performance_metrics": {
    "uptime": "99.9%",
    "avg_response_time": "0.5s", 
    "error_rate": "0.1%"
  }
}
```

---

## 👥 **SESSION MANAGEMENT**

### **Create Session**
Create user session for tracking and analytics.

```http
GET /api/session/create
```

**Response:**
```json
{
  "session_id": "sess_abc123def456",
  "status": "created"
}
```

---

## 🏥 **SYSTEM HEALTH**

### **Health Check**
System health and service status monitoring.

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "3.0.0", 
  "architecture": "ultra-lightweight",
  "platform": "huggingface-spaces",
  "timestamp": "2024-01-15T10:30:00Z",
  "services": {
    "text_generation": "active",
    "image_generation": "active", 
    "translation": "active",
    "analysis": "active",
    "termux_integration": "active"
  }
}
```

---

## 📋 **API INFORMATION**

### **Platform Info**
Comprehensive API and platform information.

```http
GET /api/info
```

**Response:**
```json
{
  "platform": "The New Civilization",
  "version": "3.0.0",
  "architecture": "API-first, ultra-lightweight",
  "philosophy": "Zero heavy dependencies, maximum efficiency", 
  "integration": "Termux mobile orchestration + HuggingFace cloud processing",
  "revenue_model": "$1K-10K monthly through AI services",
  "endpoints": {
    "text": ["/api/text/generate", "/api/text/chat"],
    "image": ["/api/image/generate"],
    "translation": ["/api/translate"], 
    "analysis": ["/api/analyze"],
    "termux": ["/api/termux/status", "/api/termux/execute"],
    "revenue": ["/api/revenue/stats", "/api/revenue/dashboard"]
  }
}
```

---

## 💸 **PRICING & COSTS**

### **Service Pricing (USD)**
| Service | Cost per Request | Premium Cost |
|---------|------------------|--------------|
| Text Generation | $0.05 | $0.08 |
| Chat Completion | $0.03 | $0.05 |
| Image Generation | $0.10 | $0.15 |
| Translation | $0.02 | $0.03 |
| Text Analysis | $0.03 | $0.05 |
| Termux Commands | $0.01 | $0.02 |

### **Subscription Tiers**
| Tier | Monthly Cost | Requests Included | Features |
|------|-------------|-------------------|----------|
| Free | $0 | 100 | Basic services |
| Starter | $29 | 1,000 | Basic + Chat |
| Pro | $99 | 5,000 | All + Priority (20% discount) |
| Enterprise | $299 | 25,000 | All + Custom + Support (40% discount) |

---

## 🔧 **TERMUX INTEGRATION EXAMPLES**

### **Python urllib Examples**
```python
import urllib.request
import urllib.parse  
import json

# Text generation
def generate_text(prompt):
    url = "https://elmatador0197-my-oasis-agent.hf.space/api/text/generate"
    data = {"text": prompt, "max_length": 100}
    
    req = urllib.request.Request(url, 
                               data=json.dumps(data).encode(),
                               headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

# Chat completion  
def chat(message):
    url = "https://elmatador0197-my-oasis-agent.hf.space/api/text/chat"
    data = {"text": message}
    
    req = urllib.request.Request(url,
                               data=json.dumps(data).encode(), 
                               headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())

# Translation
def translate(text, target="id"):
    url = "https://elmatador0197-my-oasis-agent.hf.space/api/translate" 
    data = {"text": text, "target_lang": target}
    
    req = urllib.request.Request(url,
                               data=json.dumps(data).encode(),
                               headers={'Content-Type': 'application/json'})
    
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode())
```

### **cURL Examples**
```bash
# Text generation
curl -X POST https://elmatador0197-my-oasis-agent.hf.space/api/text/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Create a story about AI", "max_length": 100}'

# Chat completion
curl -X POST https://elmatador0197-my-oasis-agent.hf.space/api/text/chat \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, how are you?"}'

# Translation
curl -X POST https://elmatador0197-my-oasis-agent.hf.space/api/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "target_lang": "id"}'

# Revenue stats
curl https://elmatador0197-my-oasis-agent.hf.space/api/revenue/stats
```

---

## ⚡ **Performance & Limits**

### **Response Times**
- Text Generation: ~0.5-2s
- Image Generation: ~3-10s  
- Translation: ~0.3-1s
- Analysis: ~0.2-0.8s

### **Rate Limits**
- Free Tier: 100 requests/month
- Starter: 1,000 requests/month
- Pro: 5,000 requests/month  
- Enterprise: 25,000 requests/month

### **Concurrent Requests**
- Maximum: 10 concurrent requests per user
- Queue: Automatic queueing for excess requests
- Priority: Paid tiers get processing priority

---

## 🚨 **Error Handling**

### **Common Error Codes**
```json
{
  "error": "HTTP 400: Bad Request",
  "detail": "Invalid request parameters",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### **Error Types**
- `400` - Bad Request (invalid parameters)
- `401` - Unauthorized (missing/invalid session)
- `429` - Rate Limit Exceeded  
- `500` - Internal Server Error
- `503` - Service Unavailable (model loading)

---

## 📞 **Support & Resources**

- **📖 Full Documentation**: [README.md](./README.md)
- **🚀 Quick Start Guide**: [QUICKSTART.md](./docs/QUICKSTART.md)
- **🛠 Deployment Guide**: [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) 
- **💰 Revenue Model**: [REVENUE_MODEL.md](./docs/REVENUE_MODEL.md)
- **🐛 Report Issues**: [GitHub Issues](https://github.com/yourusername/the-new-civilization/issues)

---

*Last updated: 2024-01-15 | API Version: 3.0.0*