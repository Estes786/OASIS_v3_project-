#!/usr/bin/env python3
"""
OASIS 2.0 Ultra-Lightweight Revolution
Termux Command Center

Interactive CLI interface for Termux that provides dashboard, monitoring, 
and control capabilities for the entire OASIS ecosystem.

Author: OASIS Development Team
Version: 2.0.0
License: MIT
"""

import os
import sys
import json
import time
import requests
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path
import threading
import subprocess

# Try to import colorama for colored output
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORS_AVAILABLE = True
except ImportError:
    COLORS_AVAILABLE = False
    # Fallback color codes
    class Fore:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        MAGENTA = '\033[95m'
        CYAN = '\033[96m'
        WHITE = '\033[97m'
        RESET = '\033[0m'

    class Style:
        BRIGHT = '\033[1m'
        RESET_ALL = '\033[0m'

# Import OASIS components
try:
    from hf_spaces_orchestrator import SpaceOrchestrator, HuggingFaceAPI
    from business_revenue_engine import BusinessAutomation
    from api_gateway_controller import OASISAPIGateway
    OASIS_COMPONENTS_AVAILABLE = True
except ImportError:
    OASIS_COMPONENTS_AVAILABLE = False

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('~/oasis_2.0/logs/command_center.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class OASISCommandCenter:
    """Main command center interface for OASIS 2.0"""

    def __init__(self, config_path: str = "~/oasis_2.0/config/.env"):
        self.config_path = Path(config_path).expanduser()
        self.running = True
        self.last_update = datetime.now()

        # Initialize components
        self.orchestrator = None
        self.business = None
        self.gateway = None
        self.gateway_thread = None

        self.load_config()
        self.initialize_components()

        print(f"{Fore.CYAN}{Style.BRIGHT}OASIS 2.0 Command Center Initialized{Style.RESET_ALL}")

    def load_config(self):
        """Load configuration from .env file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    for line in f:
                        if '=' in line and not line.strip().startswith('#'):
                            key, value = line.strip().split('=', 1)
                            os.environ[key] = value.strip('"')
                logger.info(f"Configuration loaded from {self.config_path}")
            else:
                logger.warning(f"Configuration file not found: {self.config_path}")
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")

    def initialize_components(self):
        """Initialize OASIS components"""
        if not OASIS_COMPONENTS_AVAILABLE:
            print(f"{Fore.YELLOW}⚠️  OASIS components not available. Running in limited mode.{Style.RESET_ALL}")
            return

        try:
            # Initialize orchestrator
            self.orchestrator = SpaceOrchestrator(str(self.config_path))

            # Initialize business automation
            self.business = BusinessAutomation(str(self.config_path))

            print(f"{Fore.GREEN}✅ OASIS components initialized successfully{Style.RESET_ALL}")

        except Exception as e:
            logger.error(f"Failed to initialize components: {e}")
            print(f"{Fore.RED}❌ Component initialization failed: {e}{Style.RESET_ALL}")

    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        """Print OASIS banner"""
        banner = f"""
{Fore.CYAN}{Style.BRIGHT}
╔══════════════════════════════════════════════════════════════════════╗
║                    OASIS 2.0 ULTRA-LIGHTWEIGHT                      ║
║                        REVOLUTION COMMAND CENTER                     ║
║                                                                      ║
║  🚀 Termux Orchestrator  │  🤖 Hugging Face AI  │  💰 Revenue Engine ║
╚══════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
        """
        print(banner)

    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        status = {
            'timestamp': datetime.now().isoformat(),
            'uptime': str(datetime.now() - self.last_update),
            'system': {},
            'oasis': {},
            'services': {}
        }

        # System information
        try:
            # Battery status (Android)
            battery_cmd = "cat /sys/class/power_supply/battery/capacity 2>/dev/null"
            battery = subprocess.getoutput(battery_cmd) or "Unknown"

            # Memory usage
            memory_cmd = "cat /proc/meminfo | grep MemAvailable | awk '{print $2}'"
            memory_kb = subprocess.getoutput(memory_cmd) or "0"
            memory_mb = int(memory_kb) // 1024 if memory_kb.isdigit() else 0

            # Storage space
            storage_cmd = "df -h $HOME | tail -1 | awk '{print $4}'"
            storage = subprocess.getoutput(storage_cmd) or "Unknown"

            status['system'] = {
                'battery_level': f"{battery}%",
                'available_memory': f"{memory_mb}MB",
                'available_storage': storage,
                'network_status': self.check_network_connectivity()
            }

        except Exception as e:
            logger.error(f"Failed to get system status: {e}")
            status['system'] = {'error': str(e)}

        # OASIS components status
        if OASIS_COMPONENTS_AVAILABLE:
            try:
                if self.orchestrator:
                    orchestrator_status = self.orchestrator.get_orchestrator_status()
                    status['oasis']['orchestrator'] = {
                        'registered_spaces': orchestrator_status.get('registered_spaces', 0),
                        'monitoring_active': orchestrator_status.get('monitoring_active', False)
                    }

                if self.business:
                    business_report = self.business.generate_business_report()
                    metrics = business_report.get('revenue_metrics', {})
                    status['oasis']['business'] = {
                        'monthly_revenue': metrics.get('monthly_revenue', 0),
                        'active_clients': metrics.get('active_clients', 0),
                        'total_transactions': metrics.get('total_transactions', 0)
                    }

                # Check API Gateway
                gateway_status = self.check_api_gateway_status()
                status['services']['api_gateway'] = gateway_status

            except Exception as e:
                logger.error(f"Failed to get OASIS status: {e}")
                status['oasis']['error'] = str(e)

        return status

    def check_network_connectivity(self) -> str:
        """Check network connectivity"""
        try:
            response = requests.get('https://httpbin.org/ip', timeout=5)
            if response.status_code == 200:
                return "Connected"
        except:
            pass
        return "Offline"

    def check_api_gateway_status(self) -> Dict[str, Any]:
        """Check API Gateway status"""
        try:
            api_port = os.getenv('API_PORT', '8080')
            response = requests.get(f'http://localhost:{api_port}/health', timeout=5)
            if response.status_code == 200:
                return {'status': 'running', 'port': api_port, 'data': response.json()}
        except:
            pass
        return {'status': 'stopped', 'port': api_port}

    def print_dashboard(self):
        """Print main dashboard"""
        self.clear_screen()
        self.print_banner()

        status = self.get_system_status()

        # System Status
        print(f"{Fore.YELLOW}{Style.BRIGHT}📱 SYSTEM STATUS{Style.RESET_ALL}")
        print(f"  🔋 Battery: {status['system'].get('battery_level', 'Unknown')}")
        print(f"  💾 Memory:  {status['system'].get('available_memory', 'Unknown')}")
        print(f"  💿 Storage: {status['system'].get('available_storage', 'Unknown')}")
        print(f"  📡 Network: {status['system'].get('network_status', 'Unknown')}")
        print()

        # OASIS Status
        if 'oasis' in status and not status['oasis'].get('error'):
            print(f"{Fore.GREEN}{Style.BRIGHT}🚀 OASIS STATUS{Style.RESET_ALL}")

            orch_status = status['oasis'].get('orchestrator', {})
            print(f"  🎼 Orchestrator: {orch_status.get('registered_spaces', 0)} spaces registered")
            print(f"  📊 Monitoring: {'Active' if orch_status.get('monitoring_active') else 'Inactive'}")

            biz_status = status['oasis'].get('business', {})
            print(f"  💰 Revenue: ${biz_status.get('monthly_revenue', 0):.2f}/month")
            print(f"  👥 Clients: {biz_status.get('active_clients', 0)} active")
            print(f"  📈 Transactions: {biz_status.get('total_transactions', 0)}")
            print()

        # Services Status
        print(f"{Fore.BLUE}{Style.BRIGHT}🔧 SERVICES{Style.RESET_ALL}")
        gateway_status = status['services'].get('api_gateway', {})
        gateway_state = gateway_status.get('status', 'unknown')
        gateway_color = Fore.GREEN if gateway_state == 'running' else Fore.RED
        print(f"  🌐 API Gateway: {gateway_color}{gateway_state.upper()}{Style.RESET_ALL} (port {gateway_status.get('port', 'unknown')})")
        print()

    def print_menu(self):
        """Print main menu options"""
        print(f"{Fore.CYAN}{Style.BRIGHT}COMMAND CENTER MENU{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}1.{Style.RESET_ALL} 📊 View Dashboard")
        print(f"  {Fore.WHITE}2.{Style.RESET_ALL} 🎼 Manage Orchestrator")
        print(f"  {Fore.WHITE}3.{Style.RESET_ALL} 💰 Business Management")
        print(f"  {Fore.WHITE}4.{Style.RESET_ALL} 🌐 API Gateway Control")
        print(f"  {Fore.WHITE}5.{Style.RESET_ALL} 🛠️  System Tools")
        print(f"  {Fore.WHITE}6.{Style.RESET_ALL} ⚙️  Configuration")
        print(f"  {Fore.WHITE}0.{Style.RESET_ALL} 🚪 Exit")
        print()

    def handle_orchestrator_menu(self):
        """Handle orchestrator management menu"""
        while True:
            self.clear_screen()
            print(f"{Fore.MAGENTA}{Style.BRIGHT}🎼 ORCHESTRATOR MANAGEMENT{Style.RESET_ALL}")
            print()

            if not self.orchestrator:
                print(f"{Fore.RED}❌ Orchestrator not available{Style.RESET_ALL}")
                input("Press Enter to return...")
                break

            print(f"  {Fore.WHITE}1.{Style.RESET_ALL} Register HF Space")
            print(f"  {Fore.WHITE}2.{Style.RESET_ALL} List Registered Spaces")
            print(f"  {Fore.WHITE}3.{Style.RESET_ALL} Health Check Space")
            print(f"  {Fore.WHITE}4.{Style.RESET_ALL} Start Monitoring")
            print(f"  {Fore.WHITE}5.{Style.RESET_ALL} Stop Monitoring")
            print(f"  {Fore.WHITE}0.{Style.RESET_ALL} Back to Main Menu")
            print()

            choice = input("Select option: ").strip()

            if choice == '0':
                break
            elif choice == '1':
                space_name = input("Enter space name (owner/space): ").strip()
                if space_name:
                    success = self.orchestrator.register_space(space_name)
                    if success:
                        print(f"{Fore.GREEN}✅ Space registered successfully{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}❌ Failed to register space{Style.RESET_ALL}")
                    input("Press Enter to continue...")

            elif choice == '2':
                status = self.orchestrator.get_orchestrator_status()
                spaces = status.get('spaces', {})
                if spaces:
                    print(f"\n{Fore.CYAN}Registered Spaces:{Style.RESET_ALL}")
                    for name, space_info in spaces.items():
                        print(f"  • {name} - {space_info.get('status', 'unknown')}")
                else:
                    print(f"{Fore.YELLOW}No spaces registered{Style.RESET_ALL}")
                input("\nPress Enter to continue...")

            elif choice == '3':
                space_name = input("Enter space name to check: ").strip()
                if space_name:
                    health = self.orchestrator.check_space_health(space_name)
                    print(f"\n{Fore.CYAN}Health Status:{Style.RESET_ALL}")
                    print(json.dumps(health, indent=2, default=str))
                    input("\nPress Enter to continue...")

            elif choice == '4':
                self.orchestrator.start_monitoring()
                print(f"{Fore.GREEN}✅ Monitoring started{Style.RESET_ALL}")
                input("Press Enter to continue...")

            elif choice == '5':
                self.orchestrator.stop_monitoring()
                print(f"{Fore.YELLOW}⚠️ Monitoring stopped{Style.RESET_ALL}")
                input("Press Enter to continue...")

    def handle_business_menu(self):
        """Handle business management menu"""
        while True:
            self.clear_screen()
            print(f"{Fore.GREEN}{Style.BRIGHT}💰 BUSINESS MANAGEMENT{Style.RESET_ALL}")
            print()

            if not self.business:
                print(f"{Fore.RED}❌ Business engine not available{Style.RESET_ALL}")
                input("Press Enter to return...")
                break

            print(f"  {Fore.WHITE}1.{Style.RESET_ALL} View Revenue Report")
            print(f"  {Fore.WHITE}2.{Style.RESET_ALL} Register New Client")
            print(f"  {Fore.WHITE}3.{Style.RESET_ALL} Process Test Transaction")
            print(f"  {Fore.WHITE}4.{Style.RESET_ALL} View Pricing Models")
            print(f"  {Fore.WHITE}5.{Style.RESET_ALL} Revenue Projection")
            print(f"  {Fore.WHITE}0.{Style.RESET_ALL} Back to Main Menu")
            print()

            choice = input("Select option: ").strip()

            if choice == '0':
                break
            elif choice == '1':
                report = self.business.generate_business_report()
                print(f"\n{Fore.CYAN}Revenue Report:{Style.RESET_ALL}")
                print(json.dumps(report, indent=2, default=str))
                input("\nPress Enter to continue...")

            elif choice == '2':
                name = input("Client name: ").strip()
                email = input("Client email: ").strip()
                tier = input("Client tier (basic/premium/enterprise): ").strip() or 'basic'

                if name and email:
                    client_id = self.business.client_manager.register_client(name, email, tier)
                    client = self.business.client_manager.get_client(client_id)
                    print(f"\n{Fore.GREEN}✅ Client registered:{Style.RESET_ALL}")
                    print(f"  Client ID: {client_id}")
                    print(f"  API Key: {client.api_key}")
                    input("\nPress Enter to continue...")

            elif choice == '3':
                client_id = input("Client ID: ").strip()
                service = input("Service type: ").strip()
                units = input("Units: ").strip()

                if client_id and service and units.isdigit():
                    result = self.business.process_service_request(client_id, service, int(units))
                    print(f"\n{Fore.CYAN}Transaction Result:{Style.RESET_ALL}")
                    print(json.dumps(result, indent=2))
                    input("\nPress Enter to continue...")

            elif choice == '4':
                services = ['content_generation', 'sentiment_analysis', 'document_summarization', 'translation', 'ai_chat']
                print(f"\n{Fore.CYAN}Pricing Models:{Style.RESET_ALL}")
                for service in services:
                    info = self.business.pricing_engine.get_pricing_info(service)
                    print(f"\n{service}:")
                    print(json.dumps(info, indent=2))
                input("\nPress Enter to continue...")

            elif choice == '5':
                days = input("Projection days (default 90): ").strip()
                days = int(days) if days.isdigit() else 90

                projections = self.business.simulate_revenue_growth(days)
                print(f"\n{Fore.CYAN}Revenue Projections (last 10 days):{Style.RESET_ALL}")
                for proj in projections[-10:]:
                    day = proj['day']
                    revenue = proj['projected_daily_revenue']
                    monthly = proj['projected_monthly_revenue']
                    print(f"Day {day}: ${revenue:.2f}/day → ${monthly:.2f}/month")
                input("\nPress Enter to continue...")

    def handle_gateway_menu(self):
        """Handle API gateway control menu"""
        while True:
            self.clear_screen()
            print(f"{Fore.BLUE}{Style.BRIGHT}🌐 API GATEWAY CONTROL{Style.RESET_ALL}")
            print()

            gateway_status = self.check_api_gateway_status()
            status_text = gateway_status.get('status', 'unknown')
            status_color = Fore.GREEN if status_text == 'running' else Fore.RED

            print(f"Current Status: {status_color}{status_text.upper()}{Style.RESET_ALL}")
            print()

            print(f"  {Fore.WHITE}1.{Style.RESET_ALL} Start API Gateway")
            print(f"  {Fore.WHITE}2.{Style.RESET_ALL} Stop API Gateway")
            print(f"  {Fore.WHITE}3.{Style.RESET_ALL} View Gateway Logs")
            print(f"  {Fore.WHITE}4.{Style.RESET_ALL} Test API Endpoint")
            print(f"  {Fore.WHITE}0.{Style.RESET_ALL} Back to Main Menu")
            print()

            choice = input("Select option: ").strip()

            if choice == '0':
                break
            elif choice == '1':
                self.start_api_gateway()
                input("Press Enter to continue...")
            elif choice == '2':
                self.stop_api_gateway()
                input("Press Enter to continue...")
            elif choice == '3':
                self.view_gateway_logs()
                input("Press Enter to continue...")
            elif choice == '4':
                self.test_api_endpoint()
                input("Press Enter to continue...")

    def start_api_gateway(self):
        """Start API Gateway in background thread"""
        if self.gateway_thread and self.gateway_thread.is_alive():
            print(f"{Fore.YELLOW}⚠️ Gateway is already running{Style.RESET_ALL}")
            return

        try:
            if OASIS_COMPONENTS_AVAILABLE:
                def run_gateway():
                    self.gateway = OASISAPIGateway()
                    self.gateway.start_server()

                self.gateway_thread = threading.Thread(target=run_gateway, daemon=True)
                self.gateway_thread.start()

                time.sleep(2)  # Give it time to start
                print(f"{Fore.GREEN}✅ API Gateway started{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}❌ OASIS components not available{Style.RESET_ALL}")

        except Exception as e:
            logger.error(f"Failed to start gateway: {e}")
            print(f"{Fore.RED}❌ Failed to start gateway: {e}{Style.RESET_ALL}")

    def stop_api_gateway(self):
        """Stop API Gateway"""
        try:
            if self.gateway and hasattr(self.gateway, 'server'):
                self.gateway.server.shutdown()
                print(f"{Fore.YELLOW}⚠️ API Gateway stopped{Style.RESET_ALL}")
            else:
                print(f"{Fore.YELLOW}⚠️ No gateway instance to stop{Style.RESET_ALL}")
        except Exception as e:
            logger.error(f"Failed to stop gateway: {e}")
            print(f"{Fore.RED}❌ Failed to stop gateway: {e}{Style.RESET_ALL}")

    def view_gateway_logs(self):
        """View API Gateway logs"""
        log_file = Path("~/oasis_2.0/logs/api_gateway.log").expanduser()
        if log_file.exists():
            print(f"\n{Fore.CYAN}API Gateway Logs (last 20 lines):{Style.RESET_ALL}")
            try:
                with open(log_file, 'r') as f:
                    lines = f.readlines()
                    for line in lines[-20:]:
                        print(line.strip())
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to read logs: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}⚠️ No log file found{Style.RESET_ALL}")

    def test_api_endpoint(self):
        """Test API endpoint"""
        port = os.getenv('API_PORT', '8080')
        endpoint = input(f"Test endpoint (e.g., /health): ").strip() or '/health'

        try:
            url = f"http://localhost:{port}{endpoint}"
            response = requests.get(url, timeout=5)

            print(f"\n{Fore.CYAN}Response:{Style.RESET_ALL}")
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2)}")

        except Exception as e:
            print(f"{Fore.RED}❌ Request failed: {e}{Style.RESET_ALL}")

    def handle_system_tools(self):
        """Handle system tools menu"""
        while True:
            self.clear_screen()
            print(f"{Fore.CYAN}{Style.BRIGHT}🛠️ SYSTEM TOOLS{Style.RESET_ALL}")
            print()

            print(f"  {Fore.WHITE}1.{Style.RESET_ALL} System Health Check")
            print(f"  {Fore.WHITE}2.{Style.RESET_ALL} Clean Logs")
            print(f"  {Fore.WHITE}3.{Style.RESET_ALL} Backup Data")
            print(f"  {Fore.WHITE}4.{Style.RESET_ALL} Update OASIS")
            print(f"  {Fore.WHITE}5.{Style.RESET_ALL} Restart Services")
            print(f"  {Fore.WHITE}0.{Style.RESET_ALL} Back to Main Menu")
            print()

            choice = input("Select option: ").strip()

            if choice == '0':
                break
            elif choice == '1':
                self.run_health_check()
                input("Press Enter to continue...")
            elif choice == '2':
                self.clean_logs()
                input("Press Enter to continue...")
            elif choice == '3':
                self.backup_data()
                input("Press Enter to continue...")
            elif choice == '4':
                print(f"{Fore.YELLOW}⚠️ Update feature coming soon{Style.RESET_ALL}")
                input("Press Enter to continue...")
            elif choice == '5':
                print(f"{Fore.YELLOW}⚠️ Restart feature coming soon{Style.RESET_ALL}")
                input("Press Enter to continue...")

    def run_health_check(self):
        """Run comprehensive system health check"""
        print(f"{Fore.CYAN}Running system health check...{Style.RESET_ALL}")

        # Check Python packages
        forbidden_packages = ['numpy', 'torch', 'pytorch', 'pandas', 'sklearn', 'transformers', 'gradio']
        pip_output = subprocess.getoutput("pip list")

        found_forbidden = []
        for package in forbidden_packages:
            if package in pip_output.lower():
                found_forbidden.append(package)

        if found_forbidden:
            print(f"{Fore.RED}❌ Forbidden packages detected: {', '.join(found_forbidden)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}✅ No forbidden packages detected{Style.RESET_ALL}")

        # Check disk space
        home_size = subprocess.getoutput("du -sh ~/oasis_2.0 2>/dev/null | cut -f1") or "Unknown"
        print(f"{Fore.CYAN}📁 OASIS directory size: {home_size}{Style.RESET_ALL}")

        # Check network connectivity
        network_status = self.check_network_connectivity()
        network_color = Fore.GREEN if network_status == "Connected" else Fore.RED
        print(f"{network_color}📡 Network: {network_status}{Style.RESET_ALL}")

        # Check configuration
        if self.config_path.exists():
            print(f"{Fore.GREEN}✅ Configuration file found{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Configuration file missing{Style.RESET_ALL}")

    def clean_logs(self):
        """Clean log files"""
        logs_dir = Path("~/oasis_2.0/logs").expanduser()
        if logs_dir.exists():
            try:
                for log_file in logs_dir.glob("*.log"):
                    log_file.unlink()
                print(f"{Fore.GREEN}✅ Log files cleaned{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}❌ Failed to clean logs: {e}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}⚠️ No logs directory found{Style.RESET_ALL}")

    def backup_data(self):
        """Backup OASIS data"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_cmd = f"cd ~ && tar -czf oasis_backup_{timestamp}.tar.gz oasis_2.0/data/ oasis_2.0/config/"

        try:
            subprocess.run(backup_cmd, shell=True, check=True)
            print(f"{Fore.GREEN}✅ Backup created: ~/oasis_backup_{timestamp}.tar.gz{Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}❌ Backup failed: {e}{Style.RESET_ALL}")

    def run(self):
        """Main command center loop"""
        try:
            while self.running:
                self.print_dashboard()
                self.print_menu()

                choice = input(f"{Fore.WHITE}Enter choice: {Style.RESET_ALL}").strip()

                if choice == '0':
                    self.running = False
                    print(f"{Fore.CYAN}Goodbye! OASIS 2.0 Revolution continues...{Style.RESET_ALL}")

                elif choice == '1':
                    input("\nPress Enter to refresh dashboard...")

                elif choice == '2':
                    self.handle_orchestrator_menu()

                elif choice == '3':
                    self.handle_business_menu()

                elif choice == '4':
                    self.handle_gateway_menu()

                elif choice == '5':
                    self.handle_system_tools()

                elif choice == '6':
                    print(f"{Fore.YELLOW}⚠️ Configuration editor coming soon{Style.RESET_ALL}")
                    input("Press Enter to continue...")

                else:
                    print(f"{Fore.RED}❌ Invalid choice. Please try again.{Style.RESET_ALL}")
                    time.sleep(1)

        except KeyboardInterrupt:
            print(f"\n\n{Fore.CYAN}OASIS 2.0 Command Center terminated by user.{Style.RESET_ALL}")
        except Exception as e:
            logger.error(f"Command center error: {e}")
            print(f"{Fore.RED}❌ Critical error: {e}{Style.RESET_ALL}")
        finally:
            # Cleanup
            if self.gateway:
                try:
                    self.gateway.server.shutdown()
                except:
                    pass

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="OASIS 2.0 Termux Command Center")
    parser.add_argument("--config", default="~/oasis_2.0/config/.env", help="Configuration file path")

    args = parser.parse_args()

    # Create and run command center
    command_center = OASISCommandCenter(args.config)
    command_center.run()

if __name__ == "__main__":
    main()
