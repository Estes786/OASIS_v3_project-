import urllib.request
import urllib.parse
import urllib.error
import json
import time
import os
import sys
from datetime import datetime
import uuid
import hashlib
import base64

class OASISTermuxOrchestrator:
    """Ultra-lightweight Termux orchestrator for OASIS v3"""

    def __init__(self, hf_space_url=None, config_file="oasis_config.json"):
        self.version = "3.0.0-termux-ultra-light"
        self.startup_time = datetime.now()
        self.hf_space_url = hf_space_url or "https://your-space-name.hf.space"
        self.session_id = self._generate_session_id()

        # Load configuration
        self.config = self._load_config(config_file)

        # Statistics tracking (local only)
        self.stats = {
            "requests_made": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_processing_time": 0.0,
            "session_start": self.startup_time.isoformat()
        }

        print(f"ðŸš€ OASIS v3 Termux Orchestrator v{self.version}")
        print(f"ðŸ”— Backend: {self.hf_space_url}")
        print(f"ðŸ“± Session: {self.session_id}")
        print(f"âš¡ Ultra-lightweight mode: Python + urllib only")

    def _generate_session_id(self):
        """Generate unique session identifier"""
        timestamp = str(int(time.time()))
        random_str = str(hash(timestamp + str(os.getpid())))[-6:]
        return f"termux-{random_str}"

    def _load_config(self, config_file):
        """Load configuration from file or create default"""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"âš ï¸ Config load error: {e}")

        # Default configuration
        default_config = {
            "hf_space_url": "https://your-space-name.hf.space",
            "api_endpoints": {
                "sentiment": "/api/v3/sentiment",
                "batch": "/api/v3/batch",
                "stats": "/api/v3/stats",
                "health": "/api/v3/health"
            },
            "timeout": 30,
            "max_retries": 3,
            "pricing": {
                "sentiment": 0.001,
                "batch": 0.01
            }
        }

        # Save default config
        try:
            with open(config_file, 'w') as f:
                json.dump(default_config, f, indent=2)
            print(f"ðŸ“ Default config created: {config_file}")
        except Exception as e:
            print(f"âš ï¸ Config save error: {e}")

        return default_config

    def _make_api_request(self, endpoint, data=None, method="GET"):
        """Make HTTP request to HF Spaces backend using only urllib"""
        start_time = time.time()

        try:
            url = f"{self.hf_space_url}{endpoint}"

            # Prepare request
            if data:
                # POST request with JSON data
                json_data = json.dumps(data).encode('utf-8')
                req = urllib.request.Request(
                    url, 
                    data=json_data,
                    headers={
                        'Content-Type': 'application/json',
                        'User-Agent': f'OASIS-Termux/{self.version}',
                        'X-Session-ID': self.session_id
                    }
                )
                req.get_method = lambda: 'POST'
            else:
                # GET request
                req = urllib.request.Request(
                    url,
                    headers={
                        'User-Agent': f'OASIS-Termux/{self.version}',
                        'X-Session-ID': self.session_id
                    }
                )

            # Make request with timeout
            with urllib.request.urlopen(req, timeout=self.config.get('timeout', 30)) as response:
                response_data = response.read().decode('utf-8')
                result = json.loads(response_data)

                # Update statistics
                processing_time = time.time() - start_time
                self.stats["requests_made"] += 1
                self.stats["successful_requests"] += 1
                self.stats["total_processing_time"] += processing_time

                return {
                    "success": True,
                    "data": result,
                    "processing_time": processing_time,
                    "status_code": response.getcode()
                }

        except urllib.error.HTTPError as e:
            error_msg = f"HTTP {e.code}: {e.reason}"
            print(f"âŒ HTTP Error: {error_msg}")
            self.stats["failed_requests"] += 1
            return {
                "success": False,
                "error": error_msg,
                "status_code": e.code
            }

        except urllib.error.URLError as e:
            error_msg = f"Connection error: {e.reason}"
            print(f"âŒ Connection Error: {error_msg}")
            self.stats["failed_requests"] += 1
            return {
                "success": False,
                "error": error_msg
            }

        except Exception as e:
            error_msg = f"Request failed: {str(e)}"
            print(f"âŒ Request Error: {error_msg}")
            self.stats["failed_requests"] += 1
            return {
                "success": False,
                "error": error_msg
            }

    def analyze_sentiment(self, text, model="sentiment"):
        """Analyze sentiment via HF Spaces backend"""
        print(f"ðŸ§  Analyzing sentiment: '{text[:50]}{'...' if len(text) > 50 else ''}'")

        endpoint = self.config["api_endpoints"]["sentiment"]
        data = {
            "text": text,
            "model": model
        }

        result = self._make_api_request(endpoint, data, "POST")

        if result["success"]:
            print(f"âœ… Sentiment analysis completed in {result['processing_time']:.3f}s")
            return result["data"]
        else:
            print(f"âŒ Sentiment analysis failed: {result.get('error', 'Unknown error')}")
            return result

    def batch_process(self, requests_list):
        """Process multiple AI tasks in batch"""
        print(f"ðŸ”„ Processing batch of {len(requests_list)} requests...")

        endpoint = self.config["api_endpoints"]["batch"]
        data = {
            "requests": requests_list
        }

        result = self._make_api_request(endpoint, data, "POST")

        if result["success"]:
            print(f"âœ… Batch processing completed in {result['processing_time']:.3f}s")
            return result["data"]
        else:
            print(f"âŒ Batch processing failed: {result.get('error', 'Unknown error')}")
            return result

    def health_check(self):
        """Check HF Spaces backend health"""
        print("ðŸ¥ Checking backend health...")

        endpoint = self.config["api_endpoints"]["health"]
        result = self._make_api_request(endpoint)

        if result["success"]:
            print("âœ… Backend is healthy")
            return result["data"]
        else:
            print(f"âŒ Health check failed: {result.get('error', 'Unknown error')}")
            return result

    def get_stats(self):
        """Get system statistics"""
        print("ðŸ“Š Retrieving system statistics...")

        # Local stats
        uptime = datetime.now() - self.startup_time
        local_stats = {
            "termux_orchestrator": {
                "version": self.version,
                "session_id": self.session_id,
                "uptime_seconds": uptime.total_seconds(),
                "local_stats": self.stats
            }
        }

        # Remote stats from HF Spaces
        endpoint = self.config["api_endpoints"]["stats"]
        result = self._make_api_request(endpoint)

        if result["success"]:
            print("âœ… Statistics retrieved successfully")
            # Combine local and remote stats
            combined_stats = {**local_stats, "hf_backend": result["data"]}
            return combined_stats
        else:
            print(f"âš ï¸ Could not retrieve remote stats: {result.get('error')}")
            return local_stats

    def interactive_mode(self):
        """Interactive command-line interface"""
        print("\nðŸŽ® OASIS v3 Interactive Mode")
        print("=" * 40)
        print("Commands:")
        print("  sentiment <text>     - Analyze sentiment")
        print("  health              - Check backend health")
        print("  stats               - Show statistics")
        print("  batch               - Process batch requests")
        print("  config              - Show configuration")
        print("  exit                - Exit orchestrator")
        print()

        while True:
            try:
                command = input("OASIS> ").strip().lower()

                if command == "exit":
                    print("ðŸ‘‹ Goodbye!")
                    break

                elif command == "health":
                    result = self.health_check()
                    print(json.dumps(result, indent=2))

                elif command == "stats":
                    result = self.get_stats()
                    print(json.dumps(result, indent=2))

                elif command == "config":
                    print(json.dumps(self.config, indent=2))

                elif command.startswith("sentiment "):
                    text = command[10:]  # Remove "sentiment " prefix
                    if text:
                        result = self.analyze_sentiment(text)
                        print(json.dumps(result, indent=2))
                    else:
                        print("âŒ Please provide text for sentiment analysis")

                elif command == "batch":
                    print("ðŸ“ Enter batch requests (one per line, empty line to finish):")
                    requests = []
                    while True:
                        line = input("  Request: ").strip()
                        if not line:
                            break
                        requests.append({
                            "type": "sentiment",
                            "data": line,
                            "id": str(uuid.uuid4())[:8]
                        })

                    if requests:
                        result = self.batch_process(requests)
                        print(json.dumps(result, indent=2))
                    else:
                        print("âŒ No requests provided")

                elif command == "":
                    continue  # Empty command, do nothing

                else:
                    print(f"âŒ Unknown command: {command}")
                    print("Type 'exit' to quit or try other commands")

            except KeyboardInterrupt:
                print("\nðŸ‘‹ Exiting...")
                break
            except Exception as e:
                print(f"âŒ Error: {e}")

def main():
    """Main function for command-line usage"""
    import argparse

    parser = argparse.ArgumentParser(description="OASIS v3 Termux Orchestrator")
    parser.add_argument("--url", default="https://your-space-name.hf.space", 
                       help="HuggingFace Space URL")
    parser.add_argument("--config", default="oasis_config.json",
                       help="Configuration file path")
    parser.add_argument("--sentiment", help="Analyze sentiment of provided text")
    parser.add_argument("--health", action="store_true", help="Check backend health")
    parser.add_argument("--stats", action="store_true", help="Show statistics")
    parser.add_argument("--interactive", action="store_true", help="Start interactive mode")

    args = parser.parse_args()

    # Initialize orchestrator
    orchestrator = OASISTermuxOrchestrator(args.url, args.config)

    # Execute commands
    if args.sentiment:
        result = orchestrator.analyze_sentiment(args.sentiment)
        print(json.dumps(result, indent=2))

    elif args.health:
        result = orchestrator.health_check()
        print(json.dumps(result, indent=2))

    elif args.stats:
        result = orchestrator.get_stats()
        print(json.dumps(result, indent=2))

    elif args.interactive:
        orchestrator.interactive_mode()

    else:
        # Default: start interactive mode
        orchestrator.interactive_mode()

if __name__ == "__main__":
    main()

