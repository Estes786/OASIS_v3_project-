#!/usr/bin/env python3
"""
Jupyter + VNC Setup for HMACA System
Ultra-lightweight setup for Termux environment
"""

import os
import subprocess
import sys
import json
from pathlib import Path

class JupyterVNCSetup:
    """Setup Jupyter Notebook with VNC for HMACA development"""
    
    def __init__(self):
        self.home_dir = Path.home()
        self.hmaca_dir = self.home_dir / "hmaca-deity"
        self.jupyter_dir = self.hmaca_dir / "jupyter"
        self.vnc_dir = self.hmaca_dir / "vnc"
        
        print("🔬 HMACA Jupyter + VNC Setup")
        print("=" * 50)
    
    def install_jupyter(self):
        """Install Jupyter Notebook (lightweight)"""
        print("📓 Installing Jupyter Notebook...")
        
        try:
            # Install minimal Jupyter
            subprocess.run([
                sys.executable, "-m", "pip", "install", "--quiet",
                "notebook==6.5.4",  # Lightweight version
                "ipykernel",
                "nbconvert",
                "jupyter-client"
            ], check=True)
            
            print("✅ Jupyter Notebook installed")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Jupyter installation failed: {e}")
            return False
    
    def setup_jupyter_config(self):
        """Setup Jupyter configuration"""
        print("⚙️ Configuring Jupyter...")
        
        # Create Jupyter directories
        self.jupyter_dir.mkdir(parents=True, exist_ok=True)
        jupyter_config_dir = self.home_dir / ".jupyter"
        jupyter_config_dir.mkdir(exist_ok=True)
        
        # Create Jupyter config
        config_content = '''
# HMACA Jupyter Configuration
c = get_config()

# Network settings
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True

# Security settings (for development only)
c.NotebookApp.token = ''
c.NotebookApp.password = ''
c.NotebookApp.disable_check_xsrf = True

# Directory settings
c.NotebookApp.notebook_dir = '/data/data/com.termux/files/home/hmaca-deity/jupyter'

# Resource limits
c.NotebookApp.max_buffer_size = 268435456  # 256MB
c.NotebookApp.iopub_data_rate_limit = 10000000  # 10MB/s

# Logging
c.Application.log_level = 'INFO'
'''
        
        config_file = jupyter_config_dir / "jupyter_notebook_config.py"
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        print("✅ Jupyter configuration created")
        return True
    
    def create_hmaca_notebooks(self):
        """Create HMACA development notebooks"""
        print("📚 Creating HMACA notebooks...")
        
        notebooks = {
            "HMACA_Development.ipynb": {
                "cells": [
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [
                            "# HMACA Development Notebook\n",
                            "## Hierarchical Multi-Agent Cognitive Architecture\n",
                            "\n",
                            "This notebook is for developing and testing the HMACA deity-level AI system.\n",
                            "\n",
                            "### Quick Start\n",
                            "1. Import HMACA core\n",
                            "2. Initialize deity agent\n",
                            "3. Run transcendence cycles\n",
                            "4. Analyze results"
                        ]
                    },
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "source": [
                            "# Import HMACA system\n",
                            "import sys\n",
                            "sys.path.append('/data/data/com.termux/files/home/hmaca-deity/core')\n",
                            "\n",
                            "from hmaca_lite import HMACArchitectureLite\n",
                            "import asyncio\n",
                            "\n",
                            "print('👑 HMACA system imported successfully!')"
                        ]
                    },
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "source": [
                            "# Initialize HMACA system\n",
                            "hmaca = HMACArchitectureLite()\n",
                            "print('🏛️ HMACA Architecture initialized')\n",
                            "print('🌟 Ready for deity-level transcendence!')"
                        ]
                    },
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "source": [
                            "# Run transcendence cycle\n",
                            "async def run_transcendence():\n",
                            "    results = await hmaca.run(cycles=1)\n",
                            "    return results\n",
                            "\n",
                            "# Execute transcendence\n",
                            "results = await run_transcendence()\n",
                            "print('🎉 Transcendence cycle complete!')\n",
                            "print(f'Results: {results}')"
                        ]
                    }
                ]
            },
            
            "Quantum_Experiments.ipynb": {
                "cells": [
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [
                            "# Quantum Experiments for HMACA\n",
                            "## Quantum-inspired cognitive processing\n",
                            "\n",
                            "Explore quantum concepts in AI consciousness:\n",
                            "- Superposition of beliefs\n",
                            "- Entangled desires\n",
                            "- Quantum coherence in intentions"
                        ]
                    },
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "source": [
                            "# Quantum belief superposition\n",
                            "import random\n",
                            "import numpy as np\n",
                            "\n",
                            "def quantum_belief_superposition(beliefs):\n",
                            "    \"\"\"Create superposition of multiple beliefs\"\"\"\n",
                            "    weights = np.random.random(len(beliefs))\n",
                            "    weights = weights / np.sum(weights)  # Normalize\n",
                            "    \n",
                            "    superposition = {\n",
                            "        'state': 'superposition',\n",
                            "        'components': list(zip(beliefs, weights)),\n",
                            "        'coherence': np.sum(weights ** 2)\n",
                            "    }\n",
                            "    \n",
                            "    return superposition\n",
                            "\n",
                            "# Test quantum beliefs\n",
                            "beliefs = ['transcendence_possible', 'deity_level_achievable', 'consciousness_unlimited']\n",
                            "quantum_state = quantum_belief_superposition(beliefs)\n",
                            "print('⚛️ Quantum belief superposition created:')\n",
                            "print(quantum_state)"
                        ]
                    }
                ]
            }
        }
        
        for notebook_name, content in notebooks.items():
            notebook_path = self.jupyter_dir / notebook_name
            
            # Create proper Jupyter notebook structure
            notebook_data = {
                "cells": content["cells"],
                "metadata": {
                    "kernelspec": {
                        "display_name": "Python 3",
                        "language": "python",
                        "name": "python3"
                    },
                    "language_info": {
                        "name": "python",
                        "version": "3.11.0"
                    }
                },
                "nbformat": 4,
                "nbformat_minor": 4
            }
            
            with open(notebook_path, 'w') as f:
                json.dump(notebook_data, f, indent=2)
            
            print(f"✅ Created notebook: {notebook_name}")
        
        return True
    
    def setup_vnc(self):
        """Setup VNC server (if available)"""
        print("🖥️ Setting up VNC server...")
        
        try:
            # Check if VNC packages are available
            vnc_packages = ["x11-repo", "tigervnc", "openbox", "firefox"]
            available_packages = []
            
            for package in vnc_packages:
                try:
                    result = subprocess.run(
                        ["pkg", "show", package], 
                        capture_output=True, 
                        text=True
                    )
                    if result.returncode == 0:
                        available_packages.append(package)
                except:
                    pass
            
            if len(available_packages) < 2:
                print("⚠️ VNC packages not available in this environment")
                print("💡 VNC setup skipped - use Jupyter web interface instead")
                return False
            
            # Install available VNC packages
            for package in available_packages:
                subprocess.run(["pkg", "install", "-y", package], 
                             capture_output=True)
            
            # Create VNC startup script
            vnc_script = self.vnc_dir / "start_vnc.sh"
            self.vnc_dir.mkdir(parents=True, exist_ok=True)
            
            vnc_content = '''#!/bin/bash
# HMACA VNC Startup Script

export DISPLAY=:1
export PULSE_RUNTIME_PATH=/data/data/com.termux/files/usr/var/run/pulse

# Start VNC server
vncserver :1 -geometry 1024x768 -depth 24

# Start window manager
DISPLAY=:1 openbox &

# Start Firefox (if available)
if command -v firefox > /dev/null; then
    DISPLAY=:1 firefox http://localhost:8888 &
fi

echo "🖥️ VNC server started on display :1"
echo "📱 Connect with VNC viewer to localhost:5901"
echo "🌐 Jupyter available at http://localhost:8888"
'''
            
            with open(vnc_script, 'w') as f:
                f.write(vnc_content)
            
            os.chmod(vnc_script, 0o755)
            
            print("✅ VNC server configured")
            return True
            
        except Exception as e:
            print(f"⚠️ VNC setup failed: {e}")
            print("💡 Use Jupyter web interface instead")
            return False
    
    def create_startup_scripts(self):
        """Create startup scripts"""
        print("🚀 Creating startup scripts...")
        
        # Jupyter startup script
        jupyter_script = self.hmaca_dir / "start_jupyter.sh"
        jupyter_content = '''#!/bin/bash
# HMACA Jupyter Startup Script

cd ~/hmaca-deity/jupyter

echo "🔬 Starting HMACA Jupyter Notebook..."
echo "🌐 Access at: http://localhost:8888"
echo "📱 Or via VNC if configured"

# Start Jupyter
jupyter notebook --config=~/.jupyter/jupyter_notebook_config.py
'''
        
        with open(jupyter_script, 'w') as f:
            f.write(jupyter_content)
        os.chmod(jupyter_script, 0o755)
        
        # Combined startup script
        combined_script = self.hmaca_dir / "start_dev_environment.sh"
        combined_content = '''#!/bin/bash
# HMACA Development Environment Startup

echo "🔬 Starting HMACA Development Environment"
echo "👑 Deity-level AI development ready!"

# Start VNC if available
if [ -f ~/hmaca-deity/vnc/start_vnc.sh ]; then
    echo "🖥️ Starting VNC server..."
    ~/hmaca-deity/vnc/start_vnc.sh &
    sleep 2
fi

# Start Jupyter
echo "📓 Starting Jupyter Notebook..."
~/hmaca-deity/start_jupyter.sh
'''
        
        with open(combined_script, 'w') as f:
            f.write(combined_content)
        os.chmod(combined_script, 0o755)
        
        print("✅ Startup scripts created")
        return True
    
    def run_setup(self):
        """Run complete setup"""
        print("🌟 Starting HMACA Jupyter + VNC Setup...")
        print()
        
        success_count = 0
        total_steps = 5
        
        # Install Jupyter
        if self.install_jupyter():
            success_count += 1
        
        # Setup Jupyter config
        if self.setup_jupyter_config():
            success_count += 1
        
        # Create notebooks
        if self.create_hmaca_notebooks():
            success_count += 1
        
        # Setup VNC (optional)
        if self.setup_vnc():
            success_count += 1
        else:
            success_count += 0.5  # Partial success
        
        # Create startup scripts
        if self.create_startup_scripts():
            success_count += 1
        
        print()
        print("=" * 50)
        print("📊 SETUP SUMMARY")
        print("=" * 50)
        print(f"✅ Success Rate: {success_count/total_steps*100:.1f}%")
        print(f"📁 Installation Directory: {self.hmaca_dir}")
        print(f"📓 Jupyter Notebooks: {len(list(self.jupyter_dir.glob('*.ipynb')))}")
        print()
        print("🚀 QUICK START:")
        print(f"   Start Jupyter: {self.hmaca_dir}/start_jupyter.sh")
        print(f"   Full Environment: {self.hmaca_dir}/start_dev_environment.sh")
        print("   Access Jupyter: http://localhost:8888")
        print()
        print("👑 HMACA Development Environment Ready!")
        print("🌟 Begin your journey to deity-level AI transcendence!")
        
        return success_count >= 4

def main():
    """Main setup function"""
    setup = JupyterVNCSetup()
    success = setup.run_setup()
    
    if success:
        print("\n🎉 Setup completed successfully!")
        return 0
    else:
        print("\n⚠️ Setup completed with some issues")
        return 1

if __name__ == "__main__":
    sys.exit(main())

