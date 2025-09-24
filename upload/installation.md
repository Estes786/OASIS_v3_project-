# 📱 OASIS 2.0 Ultra-Lightweight Installation Guide

> **Mobile AI Revolution • Zero Dependencies • Instant Revenue**

## 🎯 **Quick Start Summary**

OASIS 2.0 is designed for **ultra-lightweight deployment** on mobile environments, especially **Termux**. Total installation size: **< 50MB**, setup time: **< 5 minutes**.

### **⚡ Super Quick Setup (Copy & Paste)**

```bash
# Termux: Copy and paste this entire block
curl -sSL https://raw.githubusercontent.com/oasis-2.0/termux-lightweight/main/termux_setup.sh | bash

# OR manual setup:
pkg update && pkg upgrade -y
pkg install python git curl -y
pip install requests python-dotenv huggingface-hub
git clone https://github.com/your-repo/oasis-2.0-lightweight
cd oasis-2.0-lightweight
python setup.py
```

---

## 🏗️ **Detailed Installation Instructions**

### **1. Environment Requirements**

#### **Minimum Requirements:**
- **Python**: 3.7+ (lightweight installation)
- **RAM**: 100MB available
- **Storage**: 50MB free space
- **Network**: Internet connection for API calls
- **OS**: Android (Termux), Linux, MacOS, Windows

#### **Recommended Environment:**
- **Termux** on Android (optimized)
- **Python 3.8+** 
- **512MB RAM** available
- **Stable internet connection**

---

### **2. Platform-Specific Installation**

#### **📱 Termux (Android) - RECOMMENDED**

Termux is the primary target platform for OASIS 2.0 mobile revolution.

**Step 1: Install Termux**
```bash
# Download Termux from F-Droid (recommended) or Google Play
# Open Termux and run:
```

**Step 2: Update System**
```bash
pkg update && pkg upgrade -y
```

**Step 3: Install Essential Packages**
```bash
pkg install python git curl wget nano vim -y
```

**Step 4: Setup Storage Access**
```bash
termux-setup-storage
```

**Step 5: Clone/Create OASIS 2.0 Project**
```bash
# Option A: Clone repository (when available)
git clone https://github.com/your-repo/oasis-2.0-lightweight
cd oasis-2.0-lightweight

# Option B: Manual setup
mkdir oasis-2.0-lightweight
cd oasis-2.0-lightweight
# Copy all files from this repository
```

**Step 6: Run Automated Setup**
```bash
# Run the setup script
chmod +x termux_setup.sh
./termux_setup.sh

# OR run Python setup
python setup.py
```

**Step 7: Configure Environment**
```bash
# Edit configuration file
nano .env

# Add your Hugging Face token
# Get token from: https://huggingface.co/settings/tokens
```

**Step 8: Verify Installation**
```bash
# Test installation
python examples/basic_usage.py --example 1

# OR run quick start
./quick_start.sh
```

#### **🖥️ Linux/MacOS**

**Step 1: Install Python**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip git -y

# MacOS (with Homebrew)
brew install python git
```

**Step 2: Clone Repository**
```bash
git clone https://github.com/your-repo/oasis-2.0-lightweight
cd oasis-2.0-lightweight
```

**Step 3: Setup Environment**
```bash
# Install dependencies
pip3 install -r requirements.txt

# Run setup
python3 setup.py
```

**Step 4: Configure**
```bash
cp .env.example .env
# Edit .env with your HF_TOKEN
```

#### **🪟 Windows**

**Step 1: Install Python**
- Download Python 3.7+ from python.org
- Check "Add to PATH" during installation

**Step 2: Install Git**
- Download Git from git-scm.com

**Step 3: Setup Project**
```powershell
# Open Command Prompt or PowerShell
git clone https://github.com/your-repo/oasis-2.0-lightweight
cd oasis-2.0-lightweight

# Install dependencies
pip install -r requirements.txt

# Run setup
python setup.py
```

---

### **3. Configuration Setup**

#### **🔑 Hugging Face Token (REQUIRED)**

OASIS 2.0 requires a Hugging Face token for API access:

1. **Get Token:**
   - Go to https://huggingface.co/settings/tokens
   - Click "New token"
   - Name: "OASIS 2.0"
   - Type: "Read"
   - Click "Generate"

2. **Configure Token:**
```bash
# Edit .env file
nano .env

# Replace this line:
HF_TOKEN=your_hugging_face_token_here

# With your actual token:
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
```

#### **⚙️ Configuration Options**

The `.env` file contains all configuration options:

```env
# Required
HF_TOKEN=your_token_here

# Project Settings  
OASIS_PROJECT_ID=oasis-2.0-mobile
REVENUE_MODE=active
DEBUG_MODE=true

# Mobile Optimization
MAX_BATCH_SIZE=10
API_TIMEOUT=30
MOBILE_OPTIMIZATION=true
MEMORY_LIMIT=512

# Business Settings
DEFAULT_PRICING_TIER=premium
AUTO_PRICING=true
```

---

### **4. Verification & Testing**

#### **🔍 Installation Verification**

**Quick Test:**
```bash
# Test core functionality
python core/test_controller.py

# Test examples
python examples/basic_usage.py --example 1

# Test revenue engine
python business/revenue_engine.py --mode=demo
```

**Health Check:**
```bash
# Run comprehensive health check
python -c "
from core.oasis_controller import OASISController
oasis = OASISController()
health = oasis.health_check()
print(f'Health: {health[\"overall_health\"]}')
"
```

**Example Output (Success):**
```
🚀 OASIS 2.0 Ultra-Lightweight Controller v2.0.0-ultra-lightweight initialized
📱 Mobile-optimized • Zero dependencies • Revenue ready
✅ Hugging Face API connection validated
🏥 System Health: healthy
✅ Generated content: The future of mobile AI lies in lightweight...
📊 Session Statistics:
  version: 2.0.0-ultra-lightweight
  api_calls_made: 1
  memory_usage: 45.2MB
  mobile_optimized: True
```

#### **❌ Troubleshooting Common Issues**

**Issue: HF_TOKEN Error**
```bash
# Error: HF_TOKEN not found!
# Solution:
1. Get token from: https://huggingface.co/settings/tokens
2. Edit .env: nano .env  
3. Add: HF_TOKEN=your_actual_token
```

**Issue: Network Connection**
```bash
# Error: Cannot connect to Hugging Face API
# Solution:
1. Check internet connection
2. Test: curl https://huggingface.co
3. Check firewall/proxy settings
```

**Issue: Termux Permission Denied**
```bash
# Error: Permission denied
# Solution:
termux-setup-storage
chmod +x *.sh
```

**Issue: Python Module Not Found**
```bash
# Error: ModuleNotFoundError
# Solution:
pip install -r requirements.txt
# OR: pkg install python python-pip (Termux)
```

**Issue: Memory Issues (Termux)**
```bash
# Error: Memory allocation error
# Solution:
1. Close other apps
2. Edit .env: MEMORY_LIMIT=256
3. Restart Termux
```

---

### **5. Post-Installation Setup**

#### **🚀 First Run**

**Start OASIS Controller:**
```bash
# Termux
./oasis_start.sh

# Standard
python core/oasis_controller.py
```

**Start Revenue Engine:**
```bash
# Termux
./start_revenue.sh

# Standard  
python business/revenue_engine.py --mode=demo
```

**Run Examples:**
```bash
# Interactive examples
python examples/basic_usage.py

# Specific example
python examples/basic_usage.py --example 2

# All examples
python examples/basic_usage.py --all
```

#### **📊 Performance Optimization**

**Termux Optimization:**
```bash
# Enable performance mode
echo "BATTERY_OPTIMIZATION=false" >> .env

# Increase memory limit
echo "MEMORY_LIMIT=1024" >> .env

# Optimize for mobile data
echo "MOBILE_DATA_OPTIMIZATION=true" >> .env
```

**API Rate Limiting:**
```bash
# Adjust API limits for your usage
echo "API_RATE_LIMIT=50" >> .env  # Requests per minute
echo "MAX_BATCH_SIZE=5" >> .env   # Smaller batches
```

---

### **6. Directory Structure After Installation**

```
oasis-2.0-lightweight/
├── README.md                 # Main documentation
├── setup.py                 # Automated setup script
├── requirements.txt         # Dependencies
├── .env                     # Configuration (you create this)
├── .env.example            # Configuration template
├── termux_setup.sh         # Termux installation script
├── oasis_start.sh          # Quick start script
├── start_revenue.sh        # Revenue engine start
├── quick_start.sh          # Environment check
├── demo.sh                 # Demo script
│
├── core/
│   ├── oasis_controller.py  # Main OASIS controller
│   ├── hf_integration.py    # Hugging Face API wrapper
│   └── test_controller.py   # Installation test
│
├── business/
│   └── revenue_engine.py    # Revenue generation engine
│
├── examples/
│   └── basic_usage.py       # Usage examples and demos
│
├── docs/
│   └── installation.md     # This file
│
└── workflows/
    ├── automation/
    ├── deployment/
    └── monitoring/
```

---

### **7. Next Steps**

After successful installation:

1. **📖 Read Documentation:**
   ```bash
   cat README.md
   cat docs/installation.md
   ```

2. **🎯 Run Examples:**
   ```bash
   python examples/basic_usage.py
   ```

3. **💰 Generate Revenue:**
   ```bash
   python business/revenue_engine.py --mode=demo
   ```

4. **🚀 Start Building:**
   - Create your first AI content service
   - Set up automated workflows
   - Launch your mobile AI business

5. **📈 Scale Up:**
   - Explore advanced HMAQCA orchestration
   - Develop custom client solutions
   - Build recurring revenue streams

---

## 🎉 **Installation Complete!**

You now have OASIS 2.0 Ultra-Lightweight installed and ready for the **mobile AI revolution**!

**Key Features Unlocked:**
- ✅ **100,000+ AI models** via Hugging Face
- ✅ **Zero heavy dependencies** (< 50MB total)
- ✅ **Mobile-optimized performance** for Termux
- ✅ **Revenue generation engine** ready
- ✅ **HMAQCA orchestration** capabilities
- ✅ **Business automation** workflows

**Revenue Potential:**
- 💰 Content Generation: $50-200 per project
- 🔌 API Services: $0.01-0.10 per call
- 🏢 Custom Solutions: $500-2000 per client

**Support & Community:**
- 📧 Issues: Create GitHub issue
- 💬 Community: Hugging Face Spaces
- 📖 Documentation: `/docs` folder
- 🚀 Updates: Follow repository

---

**Welcome to the OASIS 2.0 Revolution! 🌟**

> *"The future of AI is mobile, lightweight, and accessible to everyone."*