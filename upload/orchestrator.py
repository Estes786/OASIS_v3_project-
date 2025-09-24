#!/usr/bin/env python3
"""
OASIS v3 Termux Orchestrator
Ultra-Lightweight Mobile AI Command Center (<5MB)
Zero Heavy Dependencies - Python + urllib only
"""

import json
import urllib.request
import urllib.parse
import urllib.error
import sys
import os
import time
from typing import Dict, Optional, Any

class OasisTermuxClient:
    """Ultra-lightweight Termux client for OASIS v3 AI orchestration"""
    
    def __init__(self, config_path: str = "oasis_config.json"):
        self.config = self.load_config(config_path)
        self.base_url = self.config.get("base_url", "https://your-space.hf.space")
        self.api_key = self.config.get("api_key", "")
        self.timeout = self.config.get("timeout", 30)
        self.retries = self.config.get("retries", 3)
        
    def load_config(self, config_path: str) -> dict:
        """Load configuration from JSON file"""
        try:
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    return json.load(f)
            else:
                # Create default config
                default_config = {
                    "base_url": "https://your-space.hf.space",
                    "api_key": "",
                    "timeout": 30,
                    "retries": 3,
                    "user_id": "mobile_user",
                    "device_info": "termux_android"
                }
                with open(config_path, 'w') as f:
                    json.dump(default_config, f, indent=2)
                return default_config
        except Exception as e:
            print(f"⚠️ Config error: {e}")
            return {"base_url": "https://your-space.hf.space", "api_key": "", "timeout": 30, "retries": 3}
    
    def make_request(self, endpoint: str, method: str = "GET", data: Optional[dict] = None) -> dict:
        """Make HTTP request using only urllib (zero external dependencies)"""
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        # Prepare request data
        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'OASIS-v3-Termux/1.0',
            'Accept': 'application/json'
        }
        
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'
        
        request_data = None
        if data:
            request_data = json.dumps(data).encode('utf-8')
            headers['Content-Length'] = str(len(request_data))
        
        # Retry logic
        for attempt in range(self.retries):
            try:
                req = urllib.request.Request(url, data=request_data, headers=headers, method=method)
                
                with urllib.request.urlopen(req, timeout=self.timeout) as response:
                    response_data = response.read().decode('utf-8')
                    return {
                        "success": True,
                        "data": json.loads(response_data),
                        "status_code": response.getcode()
                    }
                    
            except urllib.error.HTTPError as e:
                error_msg = e.read().decode('utf-8') if e.fp else str(e)
                if attempt == self.retries - 1:
                    return {
                        "success": False,
                        "error": f"HTTP {e.code}: {error_msg}",
                        "status_code": e.code
                    }
                time.sleep(2 ** attempt)  # Exponential backoff
                
            except urllib.error.URLError as e:
                if attempt == self.retries - 1:
                    return {
                        "success": False,
                        "error": f"Connection error: {str(e.reason)}",
                        "status_code": 0
                    }
                time.sleep(2 ** attempt)
                
            except Exception as e:
                if attempt == self.retries - 1:
                    return {
                        "success": False,
                        "error": f"Unexpected error: {str(e)}",
                        "status_code": 0
                    }
                time.sleep(2 ** attempt)
        
        return {"success": False, "error": "Max retries exceeded", "status_code": 0}
    
    def generate_text(self, prompt: str, max_length: int = 100) -> dict:
        """Generate text using AI"""
        data = {
            "prompt": prompt,
            "max_length": max_length,
            "temperature": 0.7
        }
        return self.make_request("api/generate", "POST", data)
    
    def analyze_sentiment(self, text: str) -> dict:
        """Analyze text sentiment"""
        data = {"text": text}
        return self.make_request("api/sentiment", "POST", data)
    
    def summarize_text(self, text: str, max_length: int = 130) -> dict:
        """Summarize long text"""
        data = {
            "text": text,
            "max_length": max_length
        }
        return self.make_request("api/summarize", "POST", data)
    
    def translate_text(self, text: str, source_lang: str = "en", target_lang: str = "de") -> dict:
        """Translate text between languages"""
        data = {
            "text": text,
            "source_lang": source_lang,
            "target_lang": target_lang
        }
        return self.make_request("api/translate", "POST", data)
    
    def answer_question(self, question: str, context: str) -> dict:
        """Answer questions based on context"""
        data = {
            "question": question,
            "context": context
        }
        return self.make_request("api/qa", "POST", data)
    
    def process_business_request(self, request_type: str, business_data: dict) -> dict:
        """Process business logic requests"""
        data = {
            "request_type": request_type,
            "data": business_data
        }
        return self.make_request("api/business/process", "POST", data)
    
    def get_revenue_dashboard(self) -> dict:
        """Get revenue dashboard data"""
        return self.make_request("api/business/revenue", "GET")
    
    def get_system_status(self) -> dict:
        """Get system health status"""
        return self.make_request("api/status", "GET")

class OasisTermuxCLI:
    """Command Line Interface for OASIS Termux Client"""
    
    def __init__(self):
        self.client = OasisTermuxClient()
        self.commands = {
            "generate": self.cmd_generate,
            "sentiment": self.cmd_sentiment,
            "summarize": self.cmd_summarize,
            "translate": self.cmd_translate,
            "qa": self.cmd_qa,
            "business": self.cmd_business,
            "revenue": self.cmd_revenue,
            "status": self.cmd_status,
            "config": self.cmd_config,
            "help": self.cmd_help
        }
    
    def display_header(self):
        """Display OASIS header"""
        print("\n" + "="*60)
        print("🚀 OASIS v3 - AI Superintelligence Ecosystem")
        print("📱 Ultra-Lightweight Termux Orchestrator (<5MB)")
        print("⚡ Zero Dependencies • Cloud-First • API-Driven")
        print("="*60 + "\n")
    
    def cmd_generate(self, args: list) -> None:
        """Generate text command"""
        if not args:
            prompt = input("Enter prompt: ")
            max_length = input("Max length (default 100): ")
            max_length = int(max_length) if max_length.isdigit() else 100
        else:
            prompt = " ".join(args)
            max_length = 100
        
        print("🤖 Generating text...")
        result = self.client.generate_text(prompt, max_length)
        
        if result["success"]:
            print(f"\n✅ Generated Text:\n{result['data']}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_sentiment(self, args: list) -> None:
        """Sentiment analysis command"""
        text = " ".join(args) if args else input("Enter text for sentiment analysis: ")
        
        print("📊 Analyzing sentiment...")
        result = self.client.analyze_sentiment(text)
        
        if result["success"]:
            data = result['data']
            print(f"\n✅ Sentiment: {data.get('sentiment', 'Unknown')}")
            print(f"Confidence: {data.get('confidence', 0):.3f}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_summarize(self, args: list) -> None:
        """Text summarization command"""
        if not args:
            text = input("Enter text to summarize: ")
            max_length = input("Max summary length (default 130): ")
            max_length = int(max_length) if max_length.isdigit() else 130
        else:
            text = " ".join(args)
            max_length = 130
        
        print("📝 Summarizing text...")
        result = self.client.summarize_text(text, max_length)
        
        if result["success"]:
            print(f"\n✅ Summary:\n{result['data']}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_translate(self, args: list) -> None:
        """Translation command"""
        if len(args) < 3:
            text = input("Enter text to translate: ")
            source_lang = input("Source language (default 'en'): ") or "en"
            target_lang = input("Target language (default 'de'): ") or "de"
        else:
            source_lang, target_lang, text = args[0], args[1], " ".join(args[2:])
        
        print(f"🌍 Translating {source_lang} -> {target_lang}...")
        result = self.client.translate_text(text, source_lang, target_lang)
        
        if result["success"]:
            print(f"\n✅ Translation:\n{result['data']}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_qa(self, args: list) -> None:
        """Question answering command"""
        if not args:
            question = input("Enter your question: ")
            context = input("Enter context: ")
        else:
            question = " ".join(args)
            context = input("Enter context: ")
        
        print("🤔 Finding answer...")
        result = self.client.answer_question(question, context)
        
        if result["success"]:
            data = result['data']
            print(f"\n✅ Answer: {data.get('answer', 'No answer found')}")
            print(f"Confidence: {data.get('confidence', 0):.3f}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_business(self, args: list) -> None:
        """Business processing command"""
        if not args:
            request_type = input("Request type (content_generation/market_analysis/customer_support/revenue_optimization): ")
            business_data = {}
        else:
            request_type = args[0]
            business_data = {"topic": " ".join(args[1:]) if len(args) > 1 else "business"}
        
        print("💼 Processing business request...")
        result = self.client.process_business_request(request_type, business_data)
        
        if result["success"]:
            print(f"\n✅ Business Result:\n{json.dumps(result['data'], indent=2)}")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_revenue(self, args: list) -> None:
        """Revenue dashboard command"""
        print("💰 Fetching revenue dashboard...")
        result = self.client.get_revenue_dashboard()
        
        if result["success"]:
            data = result['data']
            print(f"\n💰 Revenue Dashboard:")
            print(f"Current Revenue: ${data.get('current_revenue', 0)}")
            print(f"Monthly Target: ${data.get('target_monthly', 50000)}")
            print(f"Growth Rate: {data.get('growth_rate', 0)}%")
        else:
            print(f"\n❌ Error: {result['error']}")
    
    def cmd_status(self, args: list) -> None:
        """System status command"""
        print("🔍 Checking system status...")
        result = self.client.get_system_status()
        
        if result["success"]:
            print(f"\n✅ System Status: Online")
            print(f"Response Time: {result.get('response_time', 'N/A')}ms")
        else:
            print(f"\n❌ System Status: {result['error']}")
    
    def cmd_config(self, args: list) -> None:
        """Configuration management"""
        if not args:
            print(f"\nCurrent Configuration:")
            print(f"Base URL: {self.client.config.get('base_url')}")
            print(f"API Key: {'Set' if self.client.config.get('api_key') else 'Not set'}")
            print(f"Timeout: {self.client.config.get('timeout')}s")
        elif args[0] == "set":
            if len(args) >= 3:
                key, value = args[1], args[2]
                self.client.config[key] = value
                # Save config
                with open("oasis_config.json", 'w') as f:
                    json.dump(self.client.config, f, indent=2)
                print(f"✅ Configuration updated: {key} = {value}")
            else:
                print("Usage: config set <key> <value>")
    
    def cmd_help(self, args: list) -> None:
        """Display help information"""
        print("\n📚 OASIS v3 Termux Commands:")
        print("generate [prompt]           - Generate AI text")
        print("sentiment <text>            - Analyze sentiment")
        print("summarize [text]            - Summarize text")
        print("translate <src> <tgt> <txt> - Translate text")
        print("qa [question]               - Answer questions")
        print("business <type> [data]      - Business processing")
        print("revenue                     - Revenue dashboard")
        print("status                      - System status")
        print("config [set <key> <val>]    - Configuration")
        print("help                        - Show this help")
        print("\nExamples:")
        print("oasis generate Create a business plan")
        print("oasis sentiment This is amazing!")
        print("oasis revenue")
        print()
    
    def run(self, args: list) -> None:
        """Run CLI command"""
        self.display_header()
        
        if not args:
            # Interactive mode
            print("🎯 Interactive Mode - Type 'help' for commands")
            while True:
                try:
                    command_input = input("\noasis> ").strip().split()
                    if not command_input:
                        continue
                    
                    command = command_input[0].lower()
                    if command in ["exit", "quit", "q"]:
                        print("👋 Goodbye!")
                        break
                    
                    if command in self.commands:
                        self.commands[command](command_input[1:])
                    else:
                        print(f"❌ Unknown command: {command}")
                        self.cmd_help([])
                        
                except KeyboardInterrupt:
                    print("\n👋 Goodbye!")
                    break
                except Exception as e:
                    print(f"❌ Error: {e}")
        else:
            # Single command mode
            command = args[0].lower()
            if command in self.commands:
                self.commands[command](args[1:])
            else:
                print(f"❌ Unknown command: {command}")
                self.cmd_help([])

def main():
    """Main entry point"""
    cli = OasisTermuxCLI()
    cli.run(sys.argv[1:])

if __name__ == "__main__":
    main()