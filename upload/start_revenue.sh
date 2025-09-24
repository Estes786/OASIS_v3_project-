#!/bin/bash
# OASIS 2.0 Revenue Generation Engine Startup
# Automated AI monetization for mobile environments

echo "💰 OASIS 2.0 Revenue Generation Engine"
echo "======================================"
echo "Automated AI Monetization • Mobile Optimized • Instant Profit"
echo ""

# Get current directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
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

print_revenue() {
    echo -e "${PURPLE}💰 $1${NC}"
}

# Check configuration
if [ ! -f ".env" ]; then
    print_error ".env file not found!"
    print_status "Run ./oasis_start.sh first to configure environment"
    exit 1
fi

if grep -q "your_hugging_face_token_here" .env; then
    print_error "Hugging Face token not configured!"
    print_status "Configure .env file first:"
    echo "  1. Edit: nano .env"
    echo "  2. Get token: https://huggingface.co/settings/tokens"
    echo "  3. Replace 'your_hugging_face_token_here' with your token"
    exit 1
fi

# Determine Python command
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

# Revenue Engine Options
echo "🎯 Revenue Generation Options:"
echo "  1. Demo Mode - Sample revenue workflows"
echo "  2. Auto Mode - Automated revenue generation"  
echo "  3. Service Mode - Ready for client requests"
echo "  4. Analytics - Revenue performance analysis"
echo "  5. Complete Demo - Full revenue demonstration"
echo ""

# Get user choice
read -p "Select mode (1-5) [default: 1]: " choice
choice=${choice:-1}

case $choice in
    1)
        MODE="demo"
        DESCRIPTION="Demo Mode - Sample Workflows"
        ;;
    2)
        MODE="auto"
        DESCRIPTION="Auto Mode - Automated Generation"
        ;;
    3)
        MODE="service"
        DESCRIPTION="Service Mode - Client Ready"
        ;;
    4)
        MODE="analytics"
        DESCRIPTION="Analytics Mode - Performance Review"
        ;;
    5)
        MODE="complete"
        DESCRIPTION="Complete Demo - Full Experience"
        ;;
    *)
        print_warning "Invalid choice, using Demo Mode"
        MODE="demo"
        DESCRIPTION="Demo Mode - Sample Workflows"
        ;;
esac

echo ""
print_status "🚀 Starting: $DESCRIPTION"
echo ""

# Revenue potential display
print_revenue "💡 Revenue Potential Overview:"
echo "  📝 Content Generation: \$50-200 per project"
echo "  🔌 API Services: \$0.01-0.10 per call"  
echo "  🏢 Custom Solutions: \$500-2000 per client"
echo "  🎯 Monthly Potential: \$5,000-50,000+"
echo ""

# Launch appropriate mode
case $MODE in
    "demo")
        print_status "Running revenue generation demo..."
        $PYTHON_CMD business/revenue_engine.py --mode=demo
        ;;
    "auto")
        print_status "Starting automated revenue generation..."
        $PYTHON_CMD business/revenue_engine.py --mode=auto
        ;;
    "service")
        print_status "Service mode ready for client requests..."
        $PYTHON_CMD business/revenue_engine.py --mode=service
        ;;
    "analytics")
        print_status "Generating revenue analytics..."
        $PYTHON_CMD -c "
from business.revenue_engine import RevenueEngine
engine = RevenueEngine()
stats = engine.get_revenue_stats()

print('\\n💰 Revenue Analytics Summary:')
print('=' * 40)

session = stats['session_summary']
print(f'Total Revenue: \${session[\"total_revenue\"]:.2f}')
print(f'Content Services: \${session[\"content_services\"]:.2f}')
print(f'API Services: \${session[\"api_services\"]:.2f}')
print(f'Custom Solutions: \${session[\"custom_solutions\"]:.2f}')
print(f'Transactions: {session[\"transaction_count\"]}')

projections = stats['projections']
print(f'\\n📈 Projections:')
print(f'Daily Potential: \${projections[\"daily_potential\"]:.2f}')
print(f'Monthly Potential: \${projections[\"monthly_potential\"]:.2f}')
print(f'Annual Potential: \${projections[\"annual_potential\"]:.2f}')

print(f'\\n🎯 Top Service: {stats[\"business_insights\"][\"top_service\"]}')
print(f'Market Position: {stats[\"business_insights\"][\"market_position\"]}')
"
        ;;
    "complete")
        print_status "Running complete revenue demonstration..."
        $PYTHON_CMD examples/revenue_demo.py --complete
        ;;
esac

# Check execution result
if [ $? -eq 0 ]; then
    echo ""
    print_success "Revenue engine completed successfully!"
    
    # Show quick stats if available
    print_status "📊 Quick Revenue Check:"
    $PYTHON_CMD -c "
try:
    from business.revenue_engine import RevenueEngine
    engine = RevenueEngine()
    stats = engine.get_revenue_stats()
    session = stats['session_summary']
    print(f'Session Revenue: \${session[\"total_revenue\"]:.2f}')
    print(f'Transactions: {session[\"transaction_count\"]}')
except:
    print('Revenue stats not available')
" 2>/dev/null
    
    echo ""
    print_revenue "🎯 Next Steps:"
    echo "  • Scale up successful workflows"
    echo "  • Target enterprise clients"
    echo "  • Automate recurring revenue"
    echo "  • Expand service offerings"
    echo ""
    print_revenue "💡 Business Tips:"
    echo "  • Content services: High margin, scalable"
    echo "  • API automation: Recurring revenue model"  
    echo "  • Custom solutions: Premium pricing"
    echo "  • Mobile-first: Competitive advantage"
    
else
    echo ""
    print_error "Revenue engine encountered issues"
    echo ""
    print_status "🔧 Troubleshooting:"
    echo "  1. Check internet connection"
    echo "  2. Verify .env configuration"  
    echo "  3. Test basic functionality: ./oasis_start.sh"
    echo "  4. Check logs above for specific errors"
    echo ""
    print_status "💡 Quick fixes:"
    echo "  • Network test: curl https://huggingface.co"
    echo "  • Token test: python -c 'import os; print(os.getenv(\"HF_TOKEN\"))'"
    echo "  • Basic test: python examples/basic_usage.py --example 1"
    
    exit 1
fi