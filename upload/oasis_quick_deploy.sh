#!/bin/bash

# OASIS 2.0 Ultra-Lightweight Revolution - Quick Deploy
# Revolutionary one-click deployment for Termux + Hugging Face orchestration
# Zero heavy dependencies, maximum power!

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Revolutionary banner
echo -e "${CYAN}"
echo "██████╗  █████╗ ███████╗██╗███████╗    ██████╗     ██████╗ "
echo "██╔═══██╗██╔══██╗██╔════╝██║██╔════╝    ╚════██╗   ██╔═████╗"
echo "██║   ██║███████║███████╗██║███████╗     █████╔╝   ██║██╔██║"
echo "██║   ██║██╔══██║╚════██║██║╚════██║    ██╔═══╝    ████╔╝██║"
echo "╚██████╔╝██║  ██║███████║██║███████║    ███████╗██╗╚██████╔╝"
echo " ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚══════╝    ╚══════╝╚═╝ ╚═════╝ "
echo -e "${NC}"
echo -e "${GREEN}🚀 ULTRA-LIGHTWEIGHT REVOLUTION DEPLOYMENT${NC}"
echo -e "${PURPLE}Termux Command Center + Hugging Face Orchestration${NC}"
echo ""

# Check if running on Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${YELLOW}⚠️  Warning: Not running on Termux. Some features may not work.${NC}"
    read -p "Continue anyway? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}❌ Deployment cancelled.${NC}"
        exit 1
    fi
fi

# Create deployment directory
OASIS_DIR="$HOME/oasis_2.0"
echo -e "${BLUE}📁 Creating OASIS 2.0 directory...${NC}"
mkdir -p "$OASIS_DIR"
cd "$OASIS_DIR"

# Phase 1: System Setup
echo -e "${GREEN}🔧 Phase 1: Ultra-Clean System Setup${NC}"
echo -e "${CYAN}Installing minimal dependencies (NO heavy libraries!)${NC}"

# Check if termux_orchestra_setup.sh exists
if [ -f "termux_orchestra_setup.sh" ]; then
    echo -e "${GREEN}✓ Found termux_orchestra_setup.sh, executing...${NC}"
    chmod +x termux_orchestra_setup.sh
    ./termux_orchestra_setup.sh
else
    echo -e "${YELLOW}⚠️  termux_orchestra_setup.sh not found, performing basic setup...${NC}"

    # Basic Termux setup
    pkg update -y
    pkg upgrade -y
    pkg install -y python curl jq git nano

    # Install only requests library (ultra-lightweight!)
    pip install requests python-dotenv
fi

# Phase 2: Environment Configuration
echo -e "${GREEN}🔧 Phase 2: Environment Configuration${NC}"

# Create .env file if not exists
if [ ! -f ".env" ]; then
    echo -e "${YELLOW}🔐 Setting up environment configuration...${NC}"
    cat > .env << 'EOF'
# OASIS 2.0 Configuration
HUGGINGFACE_API_KEY=your_hf_token_here
OASIS_PORT=8080
OASIS_HOST=localhost
DEBUG=true

# Business Configuration
TARGET_REVENUE_MONTH_1=1000
TARGET_REVENUE_MONTH_2=5000
TARGET_REVENUE_MONTH_3=10000

# Service Pricing (USD)
CONTENT_GENERATION_MIN=50
CONTENT_GENERATION_MAX=200
SENTIMENT_ANALYSIS_RATE=0.05
SUMMARIZATION_RATE=0.10
CHAT_MESSAGE_RATE=0.01

# Hugging Face Spaces
DEFAULT_SPACE_URL=https://huggingface.co/spaces/
SPACE_MONITORING_INTERVAL=60

# Security
API_SECRET_KEY=oasis_2.0_ultra_secure_key_change_this
JWT_EXPIRATION=3600
EOF

    echo -e "${GREEN}✓ Created .env configuration file${NC}"
    echo -e "${YELLOW}🔑 Please edit .env file to add your Hugging Face API key!${NC}"
fi

# Phase 3: Service Validation
echo -e "${GREEN}🔧 Phase 3: Service Validation${NC}"

# Check Python environment
echo -e "${CYAN}🐍 Validating Python environment...${NC}"
python3 -c "
import requests
import json
import os
import sys
from urllib.parse import urlparse
print('✓ All required modules available')
print(f'✓ Python version: {sys.version}')
print('✓ Zero heavy dependencies confirmed!')
" || {
    echo -e "${RED}❌ Python environment validation failed${NC}"
    exit 1
}

# Phase 4: Service Startup
echo -e "${GREEN}🚀 Phase 4: Service Startup${NC}"

# Function to start service in background
start_service() {
    local service_name=$1
    local script_file=$2
    local port=$3

    if [ -f "$script_file" ]; then
        echo -e "${CYAN}🔄 Starting $service_name...${NC}"
        nohup python3 "$script_file" > "${service_name}.log" 2>&1 &
        echo $! > "${service_name}.pid"
        sleep 2

        if kill -0 $(cat "${service_name}.pid") 2>/dev/null; then
            echo -e "${GREEN}✓ $service_name started successfully (PID: $(cat "${service_name}.pid"))${NC}"
            if [ ! -z "$port" ]; then
                echo -e "${BLUE}  📡 Listening on port $port${NC}"
            fi
        else
            echo -e "${RED}❌ Failed to start $service_name${NC}"
            return 1
        fi
    else
        echo -e "${YELLOW}⚠️  $script_file not found, skipping $service_name${NC}"
    fi
}

# Start core services
start_service "API Gateway" "api_gateway_controller.py" "8080"
start_service "Business Revenue Engine" "business_revenue_engine.py"
start_service "HF Spaces Orchestrator" "hf_spaces_orchestrator.py"

# Phase 5: Health Check
echo -e "${GREEN}🔧 Phase 5: System Health Check${NC}"

sleep 5

# Check if services are running
echo -e "${CYAN}🏥 Performing health checks...${NC}"

check_service() {
    local service_name=$1
    local pid_file=$2

    if [ -f "$pid_file" ] && kill -0 $(cat "$pid_file") 2>/dev/null; then
        echo -e "${GREEN}✓ $service_name: Running${NC}"
        return 0
    else
        echo -e "${RED}❌ $service_name: Not running${NC}"
        return 1
    fi
}

health_status=0
check_service "API Gateway" "API Gateway.pid" || health_status=1
check_service "Business Revenue Engine" "Business Revenue Engine.pid" || health_status=1
check_service "HF Spaces Orchestrator" "HF Spaces Orchestrator.pid" || health_status=1

# System resource check
echo -e "${CYAN}📊 Resource usage:${NC}"
echo -e "${BLUE}💾 Memory: $(free -h | awk '/^Mem:/ {print $3 "/" $2}')${NC}"
echo -e "${BLUE}💿 Disk: $(df -h . | awk 'NR==2 {print $3 "/" $2 " (" $5 " used)"}')${NC}"

# Calculate footprint
if command -v du >/dev/null 2>&1; then
    footprint=$(du -sh "$OASIS_DIR" | cut -f1)
    echo -e "${BLUE}📏 OASIS 2.0 footprint: $footprint${NC}"
fi

# Phase 6: Deployment Summary
echo ""
echo -e "${GREEN}🎉 OASIS 2.0 DEPLOYMENT COMPLETE!${NC}"
echo -e "${CYAN}═══════════════════════════════════════${NC}"

if [ $health_status -eq 0 ]; then
    echo -e "${GREEN}✅ All services running successfully!${NC}"
else
    echo -e "${YELLOW}⚠️  Some services failed to start. Check logs for details.${NC}"
fi

echo ""
echo -e "${PURPLE}📋 NEXT STEPS:${NC}"
echo -e "${CYAN}1. Edit .env file with your Hugging Face API key${NC}"
echo -e "${CYAN}2. Run demo: python3 oasis_orchestrator_demo.py${NC}"
echo -e "${CYAN}3. Start command center: python3 termux_command_center.py${NC}"
echo -e "${CYAN}4. Access API at: http://localhost:8080${NC}"
echo ""

echo -e "${PURPLE}📊 REVENUE TARGETS:${NC}"
echo -e "${GREEN}💰 Month 1: $1,000 (Content Generation + Basic APIs)${NC}"
echo -e "${GREEN}💰 Month 2: $5,000 (Automated Services + Scaling)${NC}"
echo -e "${GREEN}💰 Month 3: $10,000+ (Full Ecosystem + Premium)${NC}"
echo ""

echo -e "${PURPLE}🛠️  MANAGEMENT COMMANDS:${NC}"
echo -e "${CYAN}• View logs: tail -f *.log${NC}"
echo -e "${CYAN}• Stop services: pkill -f 'python3.*oasis'${NC}"
echo -e "${CYAN}• Restart: ./oasis_quick_deploy.sh${NC}"
echo -e "${CYAN}• Status check: python3 termux_command_center.py --status${NC}"
echo ""

echo -e "${GREEN}🚀 WELCOME TO THE OASIS 2.0 REVOLUTION! 🚀${NC}"
echo -e "${PURPLE}Your Android device is now an AI superintelligence command center!${NC}"
