#!/bin/bash
# OASIS 2.0 Quick Start & Environment Check
# Instant setup verification and launch assistance

echo "⚡ OASIS 2.0 Ultra-Lightweight Quick Start"
echo "========================================="
echo "Mobile AI Revolution • Zero Dependencies • Instant Revenue"
echo ""

# Color codes for better visibility
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${CYAN}[$(date +'%H:%M:%S')]${NC} $1"
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

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_revenue() {
    echo -e "${PURPLE}💰 $1${NC}"
}

# Get current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

print_status "Starting OASIS 2.0 environment check..."

# ============================================================================
# ENVIRONMENT CHECK
# ============================================================================

echo ""
print_info "🔍 Environment Analysis:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Platform detection
PLATFORM=$(uname -s)
IS_TERMUX=false

if [[ "$PREFIX" == *"com.termux"* ]] || [[ -d "/data/data/com.termux" ]]; then
    IS_TERMUX=true
    print_success "Platform: Termux (Mobile Android)"
else
    print_success "Platform: $PLATFORM"
fi

# Python check
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    PYTHON_VERSION=$(python3 --version 2>&1 | cut -d' ' -f2)
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    PYTHON_VERSION=$(python --version 2>&1 | cut -d' ' -f2)
else
    print_error "Python not found!"
    print_info "Install: pkg install python (Termux) or use system package manager"
    exit 1
fi

print_success "Python: $PYTHON_VERSION"

# Check Python version compatibility
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [[ $PYTHON_MAJOR -lt 3 ]] || [[ $PYTHON_MAJOR -eq 3 && $PYTHON_MINOR -lt 7 ]]; then
    print_warning "Python 3.7+ recommended (found $PYTHON_VERSION)"
else
    print_success "Python version compatible"
fi

# Memory check (if available)
if command -v free &> /dev/null; then
    MEMORY=$(free -h | grep Mem | awk '{print $2}')
    print_success "Memory: $MEMORY available"
elif [[ "$IS_TERMUX" == true ]]; then
    print_success "Memory: Termux optimized"
else
    print_info "Memory: Unknown (should be sufficient)"
fi

# Storage check
DISK_USAGE=$(df -h . 2>/dev/null | tail -1 | awk '{print $4}' || echo "Unknown")
print_success "Storage: $DISK_USAGE free"

# Working directory
print_success "Directory: $(pwd)"

# Network connectivity
print_status "Testing network connectivity..."
if curl -s --connect-timeout 5 https://huggingface.co > /dev/null; then
    print_success "Network: Connected to Hugging Face"
else
    print_warning "Network: Cannot reach Hugging Face API"
    print_info "Check internet connection for full functionality"
fi

# ============================================================================
# FILE STRUCTURE CHECK
# ============================================================================

echo ""
print_info "📂 Project Structure Verification:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

REQUIRED_FILES=(
    "README.md"
    "setup.py" 
    "requirements.txt"
    "core/oasis_controller.py"
    "business/revenue_engine.py"
    "examples/basic_usage.py"
)

OPTIONAL_FILES=(
    ".env"
    "termux_setup.sh"
    "oasis_start.sh"
    "start_revenue.sh"
    "QUICK_START.md"
)

# Check required files
ALL_REQUIRED_PRESENT=true
for file in "${REQUIRED_FILES[@]}"; do
    if [[ -f "$file" ]]; then
        print_success "$file"
    else
        print_error "$file (REQUIRED)"
        ALL_REQUIRED_PRESENT=false
    fi
done

# Check optional files  
for file in "${OPTIONAL_FILES[@]}"; do
    if [[ -f "$file" ]]; then
        print_success "$file"
    else
        print_info "$file (optional)"
    fi
done

if [[ "$ALL_REQUIRED_PRESENT" == false ]]; then
    print_error "Missing required files! Please check installation."
    exit 1
fi

# ============================================================================
# CONFIGURATION CHECK
# ============================================================================

echo ""
print_info "⚙️ Configuration Analysis:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check .env file
if [[ -f ".env" ]]; then
    print_success ".env file exists"
    
    # Check if configured
    if grep -q "your_hugging_face_token_here" .env; then
        print_warning "HF_TOKEN needs configuration"
        NEEDS_CONFIG=true
    else
        print_success "HF_TOKEN appears configured"
        NEEDS_CONFIG=false
    fi
    
    # Show current config (masked)
    if [[ "$NEEDS_CONFIG" == false ]]; then
        HF_TOKEN=$(grep "HF_TOKEN=" .env | cut -d= -f2)
        if [[ -n "$HF_TOKEN" && "$HF_TOKEN" != "your_hugging_face_token_here" ]]; then
            MASKED_TOKEN="${HF_TOKEN:0:3}***${HF_TOKEN: -3}"
            print_success "Token: $MASKED_TOKEN"
        fi
    fi
else
    print_warning ".env file not found"
    NEEDS_CONFIG=true
    
    if [[ -f ".env.example" ]]; then
        print_info "Creating .env from template..."
        cp .env.example .env
        print_success ".env created from template"
    fi
fi

# ============================================================================
# DEPENDENCY CHECK  
# ============================================================================

echo ""
print_info "📦 Dependencies Verification:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

REQUIRED_PACKAGES=("requests" "dotenv" "huggingface_hub")
MISSING_PACKAGES=()

for package in "${REQUIRED_PACKAGES[@]}"; do
    package_import=${package//-/_}  # Convert hyphens to underscores for import
    
    if $PYTHON_CMD -c "import $package_import" 2>/dev/null; then
        # Get version if possible
        VERSION=$($PYTHON_CMD -c "import $package_import; print(getattr($package_import, '__version__', 'installed'))" 2>/dev/null)
        print_success "$package ($VERSION)"
    else
        print_warning "$package (missing)"
        MISSING_PACKAGES+=("$package")
    fi
done

# Install missing packages if any
if [[ ${#MISSING_PACKAGES[@]} -gt 0 ]]; then
    echo ""
    print_status "Installing missing packages: ${MISSING_PACKAGES[*]}"
    
    if pip install "${MISSING_PACKAGES[@]}"; then
        print_success "Dependencies installed successfully"
    else
        print_error "Failed to install dependencies"
        print_info "Try manually: pip install requests python-dotenv huggingface-hub"
    fi
fi

# ============================================================================
# FUNCTIONALITY TEST
# ============================================================================

echo ""
print_info "🧪 Functionality Testing:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Test OASIS import
print_status "Testing OASIS Controller import..."
if $PYTHON_CMD -c "
import sys
sys.path.insert(0, '.')
from core.oasis_controller import OASISController
print('✅ Import successful')
" 2>/dev/null; then
    print_success "OASIS Controller: Import OK"
else
    print_warning "OASIS Controller: Import failed"
fi

# Test Revenue Engine import
print_status "Testing Revenue Engine import..."
if $PYTHON_CMD -c "
import sys  
sys.path.insert(0, '.')
from business.revenue_engine import RevenueEngine
print('✅ Import successful')
" 2>/dev/null; then
    print_success "Revenue Engine: Import OK"
else
    print_warning "Revenue Engine: Import failed"
fi

# ============================================================================
# CONFIGURATION ASSISTANT
# ============================================================================

if [[ "$NEEDS_CONFIG" == true ]]; then
    echo ""
    print_info "⚙️ Configuration Assistant:"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    print_warning "Hugging Face token configuration needed"
    echo ""
    print_info "Steps to configure:"
    echo "  1. 🌐 Go to: https://huggingface.co/settings/tokens"
    echo "  2. 🔑 Click 'New token'"
    echo "  3. 📝 Name: 'OASIS 2.0'"
    echo "  4. 📋 Type: 'Read'"
    echo "  5. ✅ Click 'Generate'"
    echo "  6. 📄 Copy your token (starts with 'hf_')"
    echo ""
    
    read -p "Do you want to configure .env now? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ${EDITOR:-nano} .env
        print_success "Configuration file opened for editing"
        echo ""
        print_info "After saving, restart this script to verify configuration"
        exit 0
    fi
fi

# ============================================================================
# QUICK START MENU
# ============================================================================

echo ""
print_info "🚀 OASIS 2.0 Quick Actions:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [[ "$NEEDS_CONFIG" == false ]]; then
    print_success "✅ System ready for operation!"
    echo ""
    echo "Quick actions:"
    echo "  1. 🎯 Test basic functionality"
    echo "  2. 🚀 Start OASIS Controller"
    echo "  3. 💰 Launch Revenue Engine"
    echo "  4. 📖 View documentation"
    echo "  5. 🔧 Run setup script"
    echo "  6. 📊 Check system status"
    echo ""
    
    read -p "Select action (1-6) or Enter to continue: " choice
    
    case $choice in
        1)
            print_status "Running basic functionality test..."
            $PYTHON_CMD examples/basic_usage.py --example 1
            ;;
        2)
            print_status "Starting OASIS Controller..."
            ./oasis_start.sh
            ;;
        3)
            print_status "Launching Revenue Engine..."
            ./start_revenue.sh
            ;;
        4)
            print_status "Available documentation:"
            echo "  • README.md - Main documentation"
            echo "  • QUICK_START.md - This guide"
            echo "  • docs/installation.md - Detailed setup"
            ;;
        5)
            print_status "Running setup script..."
            $PYTHON_CMD setup.py
            ;;
        6)
            print_success "System status check completed above ✅"
            ;;
        *)
            print_info "No action selected, continuing..."
            ;;
    esac
else
    print_warning "⚠️ Configuration required before operation"
    print_info "Please configure HF_TOKEN in .env file first"
fi

# ============================================================================
# FINAL STATUS & NEXT STEPS
# ============================================================================

echo ""
print_info "🎯 System Summary:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

print_success "Platform: $(if [[ "$IS_TERMUX" == true ]]; then echo "Termux (Mobile Optimized)"; else echo "$PLATFORM"; fi)"
print_success "Python: $PYTHON_VERSION"
print_success "Dependencies: $(if [[ ${#MISSING_PACKAGES[@]} -eq 0 ]]; then echo "All installed"; else echo "Some missing"; fi)"
print_success "Files: $(if [[ "$ALL_REQUIRED_PRESENT" == true ]]; then echo "Complete structure"; else echo "Missing files"; fi)"
print_success "Config: $(if [[ "$NEEDS_CONFIG" == false ]]; then echo "Ready"; else echo "Needs HF_TOKEN"; fi)"

echo ""
print_revenue "💰 Revenue Opportunities:"
echo "  📝 Content Generation: \$50-200 per project" 
echo "  🔌 API Services: \$0.01-0.10 per call"
echo "  🏢 Custom Solutions: \$500-2000 per client"
echo "  📈 Monthly Potential: \$5,000-50,000+"

echo ""
if [[ "$NEEDS_CONFIG" == false ]]; then
    print_success "🎉 OASIS 2.0 ready for AI revenue generation!"
    echo ""
    print_info "🚀 Ready commands:"
    echo "  ./oasis_start.sh      - Start OASIS Controller"
    echo "  ./start_revenue.sh    - Launch Revenue Engine"
    echo "  python examples/basic_usage.py - Run examples"
else
    print_warning "⚙️ Complete configuration first:"
    echo "  1. Edit .env: nano .env"
    echo "  2. Add HF_TOKEN from: https://huggingface.co/settings/tokens"
    echo "  3. Restart: ./quick_start.sh"
fi

echo ""
print_success "Welcome to the OASIS 2.0 Revolution! 🌟"