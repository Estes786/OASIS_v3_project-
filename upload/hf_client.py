#!/usr/bin/env python3
"""
OASIS v3 HuggingFace Spaces API Client - Ultra-Lightweight
===========================================================
Specialized client for connecting Termux orchestrator to HF Spaces backend.
Uses ONLY Python standard library + urllib for maximum compatibility.

ZERO HEAVY DEPENDENCIES - TERMUX OPTIMIZED
"""

import urllib.request
import urllib.parse
import urllib.error
import json
import time
import os
from datetime import datetime
import hashlib

class HFSpacesClient:
    """Ultra-lightweight HuggingFace Spaces API client"""
    
    def __init__(self, space_url, timeout=30):
        self.space_url = space_url.rstrip('/')
        self.timeout = timeout
        self.session_id = self._generate_session_id()
        self.request_count = 0
        
        print(f"🔗 HF Client initialized: {self.space_url}")
    
    def _generate_session_id(self):
        """Generate unique session identifier"""
        timestamp = str(int(time.time()))
        return hashlib.md5(timestamp.encode()).hexdigest()[:12]
    
    def _make_api_call(self, endpoint, payload=None, method="GET"):
        """Make API call to HuggingFace Spaces"""
        url = f"{self.space_url}/{endpoint.lstrip('/')}"
        self.request_count += 1
        
        headers = {
            'User-Agent': 'OASIS-v3-Termux/1.0',
            'Accept': 'application/json',
            'X-Session-ID': self.session_id,
            'X-Request-Count': str(self.request_count)
        }
        
        try:
            # Prepare request data
            data = None
            if payload:
                if method in ['POST', 'PUT', 'PATCH']:
                    data = json.dumps(payload).encode('utf-8')
                    headers['Content-Type'] = 'application/json'
                else:
                    # GET request with parameters
                    params = urllib.parse.urlencode(payload)
                    url += f"?{params}"
            
            # Create and execute request
            request = urllib.request.Request(url, data=data, headers=headers, method=method)
            
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                response_data = response.read().decode('utf-8')
                
                # Try to parse JSON
                try:
                    result = json.loads(response_data)
                except json.JSONDecodeError:
                    result = {"raw_response": response_data}
                
                return {
                    "success": True,
                    "status_code": response.getcode(),
                    "data": result,
                    "url": url,
                    "method": method
                }
        
        except urllib.error.HTTPError as e:
            error_details = {"error_code": e.code, "error_reason": e.reason}
            try:
                error_body = e.read().decode('utf-8')
                error_details["error_body"] = error_body
            except:
                pass
            
            return {
                "success": False,
                "error": f"HTTP {e.code}: {e.reason}",
                "details": error_details,
                "url": url,
                "method": method
            }
        
        except urllib.error.URLError as e:
            return {
                "success": False,
                "error": f"Connection error: {e.reason}",
                "url": url,
                "method": method
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": f"Request failed: {str(e)}",
                "url": url,
                "method": method
            }
    
    def ping(self):
        """Ping the HF Spaces backend"""
        result = self._make_api_call("api/health")
        if result["success"]:
            print("✅ HF Spaces: Online")
        else:
            print(f"❌ HF Spaces: {result['error']}")
        return result
    
    def sentiment_analysis(self, text, model="roberta"):
        """Perform sentiment analysis"""
        payload = {
            "text": text,
            "model": model,
            "session_id": self.session_id
        }
        
        result = self._make_api_call("api/sentiment", payload, "POST")
        
        if result["success"]:
            sentiment_data = result["data"]
            print(f"🎭 Sentiment: {sentiment_data.get('sentiment', 'Unknown')}")
        else:
            print(f"❌ Sentiment failed: {result['error']}")
        
        return result
    
    def text_generation(self, prompt, max_length=100, model="gpt2"):
        """Generate text using AI models"""
        payload = {
            "prompt": prompt,
            "max_length": max_length,
            "model": model,
            "session_id": self.session_id
        }
        
        result = self._make_api_call("api/generate", payload, "POST")
        
        if result["success"]:
            generated = result["data"].get("generated_text", "")
            print(f"✨ Generated: {generated[:60]}...")
        else:
            print(f"❌ Generation failed: {result['error']}")
        
        return result
    
    def image_classification(self, image_data, model="resnet50"):
        """Classify image using computer vision"""
        payload = {
            "image": image_data,
            "model": model,
            "session_id": self.session_id
        }
        
        result = self._make_api_call("api/classify", payload, "POST")
        
        if result["success"]:
            predictions = result["data"].get("predictions", [])
            if predictions:
                top = predictions[0]
                print(f"🖼️  Classification: {top.get('label', 'Unknown')}")
        else:
            print(f"❌ Classification failed: {result['error']}")
        
        return result
    
    def batch_process(self, tasks):
        """Process multiple tasks in batch"""
        payload = {
            "tasks": tasks,
            "session_id": self.session_id,
            "batch_size": len(tasks)
        }
        
        result = self._make_api_call("api/batch", payload, "POST")
        
        if result["success"]:
            processed = result["data"].get("processed_count", 0)
            print(f"📦 Batch: {processed}/{len(tasks)} processed")
        else:
            print(f"❌ Batch failed: {result['error']}")
        
        return result
    
    def get_models(self):
        """Get available AI models"""
        result = self._make_api_call("api/models")
        
        if result["success"]:
            models = result["data"].get("models", [])
            print(f"🧠 Available models: {len(models)}")
            for model in models:
                print(f"  - {model.get('name', 'Unknown')}: {model.get('type', 'Unknown')}")
        else:
            print(f"❌ Models fetch failed: {result['error']}")
        
        return result
    
    def get_stats(self):
        """Get backend statistics"""
        result = self._make_api_call("api/stats")
        
        if result["success"]:
            stats = result["data"]
            print(f"📊 Backend Stats:")
            print(f"  Uptime: {stats.get('uptime', 'Unknown')}")
            print(f"  Requests: {stats.get('total_requests', 0)}")
            print(f"  Load: {stats.get('current_load', 'Unknown')}")
        else:
            print(f"❌ Stats fetch failed: {result['error']}")
        
        return result
    
    def upload_file(self, file_path, endpoint="api/upload"):
        """Upload file to HF Spaces"""
        try:
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            # Simple base64 encoding for file transfer
            import base64
            encoded_file = base64.b64encode(file_data).decode('utf-8')
            
            payload = {
                "filename": os.path.basename(file_path),
                "file_data": encoded_file,
                "session_id": self.session_id
            }
            
            result = self._make_api_call(endpoint, payload, "POST")
            
            if result["success"]:
                file_id = result["data"].get("file_id", "Unknown")
                print(f"📤 Upload successful: {file_id}")
            else:
                print(f"❌ Upload failed: {result['error']}")
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "error": f"File upload error: {str(e)}"
            }
    
    def get_session_info(self):
        """Get current session information"""
        return {
            "session_id": self.session_id,
            "request_count": self.request_count,
            "space_url": self.space_url,
            "timeout": self.timeout,
            "timestamp": datetime.now().isoformat()
        }


class APITester:
    """Test suite for HF Spaces API endpoints"""
    
    def __init__(self, client):
        self.client = client
        self.test_results = []
    
    def run_all_tests(self):
        """Run comprehensive API tests"""
        print("🧪 Running API Tests...")
        print("=" * 40)
        
        tests = [
            ("Health Check", self._test_health),
            ("Sentiment Analysis", self._test_sentiment),
            ("Text Generation", self._test_generation),
            ("Model List", self._test_models),
            ("Stats Fetch", self._test_stats)
        ]
        
        for test_name, test_func in tests:
            print(f"\n🔍 {test_name}...")
            try:
                result = test_func()
                status = "✅ PASS" if result.get("success") else "❌ FAIL"
                print(f"{status}: {test_name}")
                self.test_results.append({
                    "test": test_name,
                    "success": result.get("success", False),
                    "result": result
                })
            except Exception as e:
                print(f"❌ FAIL: {test_name} - {str(e)}")
                self.test_results.append({
                    "test": test_name,
                    "success": False,
                    "error": str(e)
                })
        
        # Summary
        passed = sum(1 for t in self.test_results if t["success"])
        total = len(self.test_results)
        
        print(f"\n📋 Test Summary: {passed}/{total} tests passed")
        return self.test_results
    
    def _test_health(self):
        """Test health endpoint"""
        return self.client.ping()
    
    def _test_sentiment(self):
        """Test sentiment analysis"""
        return self.client.sentiment_analysis("This is a great day!")
    
    def _test_generation(self):
        """Test text generation"""
        return self.client.text_generation("The future of AI is", 50)
    
    def _test_models(self):
        """Test models endpoint"""
        return self.client.get_models()
    
    def _test_stats(self):
        """Test stats endpoint"""
        return self.client.get_stats()


def main():
    """Demo/test the HF Spaces client"""
    print("🔗 OASIS v3 HuggingFace Spaces Client")
    print("=" * 50)
    
    # Initialize client
    space_url = "https://elmatador0197-my-oasis-agent.hf.space"
    client = HFSpacesClient(space_url)
    
    # Run tests
    tester = APITester(client)
    results = tester.run_all_tests()
    
    # Interactive mode
    print("\n🎯 Interactive Mode (type 'quit' to exit)")
    while True:
        try:
            command = input("\nHF> ").strip().lower()
            
            if command in ['quit', 'exit']:
                break
            elif command == 'ping':
                client.ping()
            elif command == 'models':
                client.get_models()
            elif command == 'stats':
                client.get_stats()
            elif command == 'info':
                info = client.get_session_info()
                print(json.dumps(info, indent=2))
            elif command == 'test':
                tester.run_all_tests()
            else:
                print("Commands: ping, models, stats, info, test, quit")
        
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
    
    print("👋 HF Client terminated")


if __name__ == "__main__":
    main()