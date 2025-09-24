#!/bin/bash
# Make all OASIS 2.0 scripts executable
# Run this after downloading/copying files

echo "🔧 Making OASIS 2.0 scripts executable..."

# List of scripts to make executable
SCRIPTS=(
    "termux_setup.sh"
    "oasis_start.sh"
    "start_revenue.sh"
    "quick_start.sh"
    "make_executable.sh"
)

# Make scripts executable
for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        chmod +x "$script"
        echo "✅ $script is now executable"
    else
        echo "⚠️  $script not found"
    fi
done

# Make Python files executable (optional)
PYTHON_FILES=(
    "setup.py"
    "core/oasis_controller.py"
    "business/revenue_engine.py"
    "examples/basic_usage.py"
    "examples/revenue_demo.py"
)

for pyfile in "${PYTHON_FILES[@]}"; do
    if [ -f "$pyfile" ]; then
        chmod +x "$pyfile"
        echo "✅ $pyfile is now executable"
    fi
done

echo ""
echo "🎉 All scripts are now executable!"
echo ""
echo "🚀 Ready to run:"
echo "  ./quick_start.sh      - Environment check & quick start"
echo "  ./termux_setup.sh     - Full Termux setup"
echo "  ./oasis_start.sh      - Start OASIS Controller"
echo "  ./start_revenue.sh    - Launch Revenue Engine"
echo ""
echo "💡 If you just downloaded these files, also run:"
echo "  python setup.py       - Complete setup process"