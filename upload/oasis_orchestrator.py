#!/usr/bin/env python3
"""
OASIS v3 Termux Orchestrator - Ultra-Lightweight Command Center
===============================================================
Revolutionary AI orchestration using ONLY Python standard library + urllib.
Connects to HuggingFace Spaces AI backend for powerful processing.

CONSTRAINTS:
- Termux footprint: <5MB
- Dependencies: Python standard library + urllib ONLY
- All AI/ML/DL processing on HuggingFace Spaces
- Zero installation errors, zero heavy dependencies

Architecture: [TERMUX ORCHESTRATOR] ←→ [HF SPACES AI BACKEND]
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
import os
import sys
from datetime import datetime
import threading
import queue
import hashlib
import base64

class OasisOrchestrator:
    """Ultra-lightweight Termux orchestrator for OASIS v3"""
    
    def __init__(self, hf_space_url=None, config_file="oasis_config.json"):
        self.hf_space_url = hf_space_url or "https://elmatador0197-my-oasis-agent.hf.space"
        self.config_file = config_file
        self.config = self._load_config()
        self.session_id = self._generate_session_id()
        self.revenue_tracker = RevenueTracker()
        self.task_queue = queue.Queue()
        self.results = {}
        
        print(f"🚀 OASIS v3 Orchestrator initialized")
        print(f"📡 HF Spaces Backend: {self.hf_space_url}")
        print(f"💻 Session ID: {self.session_id}")
        print(f"📱 Termux footprint: <5MB (Python + urllib only)")
    
    def _load_config(self):
        """Load configuration from JSON file"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"⚠️  Config load error: {e}")
        
        # Default configuration
        return {
            "api_endpoints": {
                "sentiment": "/api/sentiment",
                "generate": "/api/generate",
                "classify": "/api/classify",
                "batch": "/api/batch"
            },
            "pricing": {
                "sentiment": 0.01,
                "generate": 0.05,
                "classify": 0.02,
                "batch": 0.10
            },
            "timeout": 30,
            "max_retries": 3
        }
    
    def _generate_session_id(self):
        """Generate unique session ID"""
        timestamp = str(int(time.time()))
        hash_obj = hashlib.md5(timestamp.encode())
        return hash_obj.hexdigest()[:8]
    
    def _make_request(self, endpoint, data, method="POST"):
        """Make HTTP request to HuggingFace Spaces backend"""
        url = f"{self.hf_space_url}{endpoint}"
        
        try:
            # Prepare data
            if isinstance(data, dict):
                json_data = json.dumps(data).encode('utf-8')
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'OASIS-v3-Termux-Orchestrator/1.0',
                    'X-Session-ID': self.session_id
                }
            else:
                json_data = str(data).encode('utf-8')
                headers = {
                    'Content-Type': 'text/plain',
                    'User-Agent': 'OASIS-v3-Termux-Orchestrator/1.0',
                    'X-Session-ID': self.session_id
                }
            
            # Create request
            req = urllib.request.Request(url, data=json_data, headers=headers, method=method)
            
            # Make request with timeout
            with urllib.request.urlopen(req, timeout=self.config['timeout']) as response:
                result = json.loads(response.read().decode('utf-8'))
                return {"success": True, "data": result}
                
        except urllib.error.HTTPError as e:
            error_msg = f"HTTP {e.code}: {e.reason}"
            try:
                error_detail = e.read().decode('utf-8')
                error_msg += f" - {error_detail}"
            except:
                pass
            return {"success": False, "error": error_msg}
            
        except urllib.error.URLError as e:
            return {"success": False, "error": f"Connection error: {e.reason}"}
            
        except Exception as e:
            return {"success": False, "error": f"Request failed: {str(e)}"}
    
    def sentiment_analysis(self, text, model="roberta"):
        """Perform sentiment analysis via HF Spaces"""
        print(f"🎭 Sentiment Analysis: {text[:50]}...")
        
        data = {
            "text": text,
            "model": model,
            "session_id": self.session_id
        }
        
        result = self._make_request(self.config['api_endpoints']['sentiment'], data)
        
        if result["success"]:
            # Track revenue
            self.revenue_tracker.add_transaction("sentiment", self.config['pricing']['sentiment'])
            print(f"✅ Sentiment: {result['data'].get('sentiment', 'N/A')} ({result['data'].get('confidence', 0):.2%})")
        else:
            print(f"❌ Sentiment analysis failed: {result['error']}")
        
        return result
    
    def text_generation(self, prompt, max_length=100, model="gpt2"):
        """Generate text via HF Spaces"""
        print(f"✨ Text Generation: {prompt[:30]}...")
        
        data = {
            "prompt": prompt,
            "max_length": max_length,
            "model": model,
            "session_id": self.session_id
        }
        
        result = self._make_request(self.config['api_endpoints']['generate'], data)
        
        if result["success"]:
            # Track revenue
            self.revenue_tracker.add_transaction("generate", self.config['pricing']['generate'])
            generated_text = result['data'].get('generated_text', '')
            print(f"✅ Generated: {generated_text[:50]}...")
        else:
            print(f"❌ Text generation failed: {result['error']}")
        
        return result
    
    def image_classification(self, image_path, model="resnet50"):
        """Classify image via HF Spaces"""
        print(f"🖼️  Image Classification: {image_path}")
        
        try:
            # Read and encode image
            with open(image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            data = {
                "image": image_data,
                "model": model,
                "session_id": self.session_id
            }
            
            result = self._make_request(self.config['api_endpoints']['classify'], data)
            
            if result["success"]:
                # Track revenue
                self.revenue_tracker.add_transaction("classify", self.config['pricing']['classify'])
                predictions = result['data'].get('predictions', [])
                if predictions:
                    top_pred = predictions[0]
                    print(f"✅ Classification: {top_pred.get('label', 'N/A')} ({top_pred.get('confidence', 0):.2%})")
            else:
                print(f"❌ Image classification failed: {result['error']}")
            
            return result
            
        except Exception as e:
            error_result = {"success": False, "error": f"Image processing error: {str(e)}"}
            print(f"❌ Image error: {str(e)}")
            return error_result
    
    def batch_processing(self, tasks):
        """Process multiple tasks in batch via HF Spaces"""
        print(f"📦 Batch Processing: {len(tasks)} tasks")
        
        data = {
            "tasks": tasks,
            "session_id": self.session_id
        }
        
        result = self._make_request(self.config['api_endpoints']['batch'], data)
        
        if result["success"]:
            # Track revenue
            self.revenue_tracker.add_transaction("batch", self.config['pricing']['batch'])
            processed = result['data'].get('processed', 0)
            print(f"✅ Batch completed: {processed}/{len(tasks)} tasks")
        else:
            print(f"❌ Batch processing failed: {result['error']}")
        
        return result
    
    def get_revenue_stats(self):
        """Get current revenue statistics"""
        stats = self.revenue_tracker.get_stats()
        print("\n💰 REVENUE STATISTICS")
        print("=" * 40)
        print(f"Total Revenue: ${stats['total_revenue']:.2f}")
        print(f"Total Transactions: {stats['total_transactions']}")
        print(f"Session Revenue: ${stats['session_revenue']:.2f}")
        print("Service Breakdown:")
        for service, revenue in stats['service_breakdown'].items():
            print(f"  {service}: ${revenue:.2f}")
        return stats
    
    def health_check(self):
        """Check HF Spaces backend health"""
        print("🔍 Health Check...")
        
        try:
            url = f"{self.hf_space_url}/api/health"
            req = urllib.request.Request(url, headers={'User-Agent': 'OASIS-v3-Health-Check'})
            
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.getcode() == 200:
                    print("✅ HF Spaces backend: HEALTHY")
                    return True
                else:
                    print(f"⚠️  HF Spaces backend: HTTP {response.getcode()}")
                    return False
                    
        except Exception as e:
            print(f"❌ HF Spaces backend: OFFLINE ({str(e)})")
            return False
    
    def run_interactive_mode(self):
        """Run interactive command mode"""
        print("\n🎯 OASIS v3 Interactive Mode")
        print("Commands: sentiment, generate, classify, batch, revenue, health, quit")
        print("=" * 60)
        
        while True:
            try:
                command = input("\n🚀 OASIS> ").strip().lower()
                
                if command in ['quit', 'exit', 'q']:
                    print("👋 OASIS Orchestrator shutting down...")
                    break
                
                elif command == 'health':
                    self.health_check()
                
                elif command == 'revenue':
                    self.get_revenue_stats()
                
                elif command == 'sentiment':
                    text = input("Enter text for sentiment analysis: ")
                    self.sentiment_analysis(text)
                
                elif command == 'generate':
                    prompt = input("Enter prompt for text generation: ")
                    max_len = input("Max length (default 100): ")
                    try:
                        max_len = int(max_len) if max_len else 100
                    except:
                        max_len = 100
                    self.text_generation(prompt, max_len)
                
                elif command == 'classify':
                    image_path = input("Enter image path: ")
                    self.image_classification(image_path)
                
                elif command == 'batch':
                    print("Batch processing - enter tasks (one per line, empty line to finish):")
                    tasks = []
                    while True:
                        task = input("Task: ").strip()
                        if not task:
                            break
                        tasks.append({"type": "sentiment", "text": task})
                    
                    if tasks:
                        self.batch_processing(tasks)
                    else:
                        print("No tasks provided")
                
                elif command == 'help':
                    print("Available commands:")
                    print("  sentiment - Analyze sentiment of text")
                    print("  generate - Generate text from prompt")
                    print("  classify - Classify image")
                    print("  batch - Process multiple tasks")
                    print("  revenue - Show revenue statistics")
                    print("  health - Check backend health")
                    print("  quit - Exit orchestrator")
                
                else:
                    print(f"Unknown command: {command}. Type 'help' for available commands.")
            
            except KeyboardInterrupt:
                print("\n👋 OASIS Orchestrator shutting down...")
                break
            except Exception as e:
                print(f"❌ Command error: {str(e)}")


class RevenueTracker:
    """Ultra-lightweight revenue tracking"""
    
    def __init__(self):
        self.transactions = []
        self.session_revenue = 0.0
        self.service_totals = {}
    
    def add_transaction(self, service, amount):
        """Add a revenue transaction"""
        transaction = {
            "service": service,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        }
        
        self.transactions.append(transaction)
        self.session_revenue += amount
        
        if service not in self.service_totals:
            self.service_totals[service] = 0.0
        self.service_totals[service] += amount
    
    def get_stats(self):
        """Get revenue statistics"""
        return {
            "total_revenue": sum(t["amount"] for t in self.transactions),
            "total_transactions": len(self.transactions),
            "session_revenue": self.session_revenue,
            "service_breakdown": self.service_totals.copy()
        }


class BusinessAutomation:
    """Business process automation for OASIS v3"""
    
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
    
    def automated_content_generation(self, topics, count=5):
        """Generate content automatically for multiple topics"""
        print(f"🤖 Automated Content Generation: {len(topics)} topics")
        
        results = []
        for topic in topics:
            prompt = f"Write a comprehensive article about {topic}:"
            result = self.orchestrator.text_generation(prompt, max_length=300)
            results.append({
                "topic": topic,
                "content": result.get("data", {}).get("generated_text", ""),
                "success": result.get("success", False)
            })
        
        success_count = sum(1 for r in results if r["success"])
        print(f"✅ Content generated: {success_count}/{len(topics)} articles")
        return results
    
    def sentiment_monitoring(self, texts):
        """Monitor sentiment across multiple texts"""
        print(f"📊 Sentiment Monitoring: {len(texts)} texts")
        
        results = []
        for text in texts:
            result = self.orchestrator.sentiment_analysis(text)
            if result["success"]:
                sentiment_data = result["data"]
                results.append({
                    "text": text[:50] + "...",
                    "sentiment": sentiment_data.get("sentiment"),
                    "confidence": sentiment_data.get("confidence"),
                    "success": True
                })
            else:
                results.append({
                    "text": text[:50] + "...",
                    "error": result["error"],
                    "success": False
                })
        
        # Analysis
        positive = sum(1 for r in results if r.get("sentiment") == "POSITIVE")
        negative = sum(1 for r in results if r.get("sentiment") == "NEGATIVE")
        neutral = sum(1 for r in results if r.get("sentiment") == "NEUTRAL")
        
        print(f"📈 Sentiment Distribution: {positive} positive, {neutral} neutral, {negative} negative")
        return results


def main():
    """Main entry point for OASIS v3 Termux Orchestrator"""
    print("🚀 OASIS v3 - Ultra-Lightweight Termux Orchestrator")
    print("=" * 60)
    print("Architecture: Termux (<5MB) ←→ HuggingFace Spaces (AI Power)")
    print("Dependencies: Python standard library + urllib ONLY")
    
    # Initialize orchestrator
    try:
        # Check for HF Space URL in command line arguments
        hf_url = None
        if len(sys.argv) > 1:
            hf_url = sys.argv[1]
        
        orchestrator = OasisOrchestrator(hf_space_url=hf_url)
        
        # Health check
        if not orchestrator.health_check():
            print("⚠️  Warning: Backend may be unavailable")
        
        # Run interactive mode
        orchestrator.run_interactive_mode()
        
    except KeyboardInterrupt:
        print("\n👋 Graceful shutdown")
    except Exception as e:
        print(f"❌ Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()