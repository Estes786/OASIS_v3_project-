#!/bin/bash
# OASIS 2.0 Ultra-Lightweight Startup Script
# Mobile AI Revolution • Zero Dependencies • Instant Revenue

echo "🚀 Starting OASIS 2.0 Ultra-Lightweight Controller"
echo "=================================================="
echo "Mobile AI Revolution • Zero Dependencies • Instant Revenue"
echo ""

# Get current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if .env exists and is configured
if [ ! -f ".env" ]; then
    print_error ".env file not found!"
    print_status "Creating .env from template..."
    
    if [ -f ".env.example" ]; then
        cp .env.example .env
        print_warning "Please configure your Hugging Face token in .env"
        print_status "Edit with: nano .env"
        print_status "Get token from: https://huggingface.co/settings/tokens"
        exit 1
    else
        print_error ".env.example not found! Please check installation."
        exit 1
    fi
fi

# Check if HF_TOKEN is configured
if grep -q "your_hugging_face_token_here" .env; then
    print_error "Hugging Face token not configured!"
    print_status "Steps to configure:"
    echo "  1. Get token from: https://huggingface.co/settings/tokens"
    echo "  2. Edit .env file: nano .env"
    echo "  3. Replace 'your_hugging_face_token_here' with your actual token"
    echo ""
    
    read -p "Do you want to edit .env now? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ${EDITOR:-nano} .env
        echo ""
        print_status "Configuration updated. Restart this script."
        exit 0
    else
        print_warning "Please configure .env manually and restart"
        exit 1
    fi
fi

# Check Python and dependencies
print_status "Checking environment..."

if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    print_error "Python not found!"
    print_status "Install with: pkg install python (Termux) or system package manager"
    exit 1
fi

# Determine Python command
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

print_success "Python found: $($PYTHON_CMD --version)"

# Check core files
CORE_FILES=("core/oasis_controller.py" "business/revenue_engine.py" "examples/basic_usage.py")

for file in "${CORE_FILES[@]}"; do
    if [ ! -f "$file" ]; then
        print_error "Core file missing: $file"
        print_status "Please check installation or download complete repository"
        exit 1
    fi
done

print_success "Core files verified"

# Check Python dependencies
print_status "Checking Python dependencies..."

REQUIRED_PACKAGES=("requests" "dotenv" "huggingface_hub")
MISSING_PACKAGES=()

for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! $PYTHON_CMD -c "import ${package//-/_}" 2>/dev/null; then
        MISSING_PACKAGES+=("$package")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -gt 0 ]; then
    print_warning "Missing packages: ${MISSING_PACKAGES[*]}"
    print_status "Installing missing packages..."
    
    if ! pip install "${MISSING_PACKAGES[@]}"; then
        print_error "Failed to install packages"
        print_status "Try manually: pip install requests python-dotenv huggingface-hub"
        exit 1
    fi
    
    print_success "Dependencies installed"
else
    print_success "All dependencies available"
fi

# Test basic functionality
print_status "Testing OASIS functionality..."

if ! $PYTHON_CMD -c "
import sys
import os
sys.path.insert(0, '.')
try:
    from core.oasis_controller import OASISController
    print('✅ OASIS Controller import successful')
except Exception as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)
" 2>/dev/null; then
    print_error "OASIS Controller test failed"
    print_status "Check your .env configuration and try again"
    exit 1
fi

print_success "OASIS Controller ready"

# Environment summary
echo ""
print_status "🎯 Environment Summary:"
echo "  📍 Working Directory: $(pwd)"
echo "  🐍 Python: $($PYTHON_CMD --version)"
echo "  📦 Dependencies: ✅ Installed"
echo "  🔑 HF Token: ✅ Configured"
echo "  📱 Platform: $(uname -s)"
echo "  💾 Memory: $(free -h 2>/dev/null | grep Mem | awk '{print $2}' || echo 'Unknown')"

echo ""
print_success "🚀 OASIS 2.0 Controller Starting..."
echo ""

# Launch OASIS Controller with error handling
if ! $PYTHON_CMD core/oasis_controller.py; then
    echo ""
    print_error "OASIS Controller failed to start"
    echo ""
    print_status "🔧 Troubleshooting steps:"
    echo "  1. Check your internet connection"
    echo "  2. Verify HF_TOKEN in .env file"
    echo "  3. Test with: python examples/basic_usage.py --example 1"
    echo "  4. Check logs above for specific error messages"
    echo ""
    print_status "💡 Common solutions:"
    echo "  • Network: curl https://huggingface.co"
    echo "  • Token: Get new token from https://huggingface.co/settings/tokens"
    echo "  • Dependencies: pip install -r requirements.txt"
    echo ""
    exit 1
fi