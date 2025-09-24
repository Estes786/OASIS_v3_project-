#!/bin/bash

# ==============================================================================
# THE NEW CIVILIZATION - Termux Setup Script (ULTRA-LIGHTWEIGHT)
# Pure API-First Environment for Mobile Revolution
# ==============================================================================

echo "🚀 THE NEW CIVILIZATION - TERMUX SETUP STARTING (ULTRA-LIGHTWEIGHT)..."
echo "========================================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️ $1${NC}"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Phase 1: System Update and Core Package Installation
echo -e "${PURPLE}📦 Phase 1: Core System Setup (Ultra-Lightweight)${NC}"
echo "----------------------------------------------------"

print_info "Updating Termux packages..."
pkg update -y && pkg upgrade -y
print_status "Package system updated"

# Install essential packages (ultra-lightweight approach)
# ONLY basic tools and Python for API interaction
ESSENTIAL_PACKAGES=(
    "python"
    "python-pip"
    "git"
    "curl"
    "wget"
    "nodejs-lts" # Node.js LTS for potential future webhooks/small servers
    "nano"
    "vim"
    "openssh"
    "rsync"
    "zip"
    "unzip"
    "jq" # For parsing JSON in bash scripts if needed
)

print_info "Installing essential packages..."
for package in "${ESSENTIAL_PACKAGES[@]}"; do
    if ! command_exists "$package"; then
        pkg install -y "$package"
        print_status "Installed $package"
    else
        print_status "$package already installed"
    fi
done

# Setup storage access
print_info "Setting up storage access..."
if [ ! -d "$HOME/storage" ]; then
    termux-setup-storage
    print_status "Storage access configured"
else
    print_status "Storage access already configured"
fi

# Phase 2: Python Environment Setup (API-First Minimal)
echo -e "${PURPLE}🐍 Phase 2: Python API Environment (Minimal)${NC}"
echo "---------------------------------------------------------"

# Upgrade pip
print_info "Upgrading pip..."
python -m pip install --upgrade pip
print_status "pip upgraded"

# Install ONLY necessary Python packages for API interaction
# No heavy AI/ML/DL frameworks here
MINIMAL_PYTHON_PACKAGES=(
    "requests"          # For making HTTP requests to Hugging Face API
    "python-dotenv"     # For managing environment variables
    "rich"              # For beautiful terminal output
    "huggingface_hub"   # For basic Hugging Face Hub interaction (e.g., listing models, login, NOT full transformers)
)

print_info "Installing minimal Python packages..."
for package in "${MINIMAL_PYTHON_PACKAGES[@]}"; do
    pip install "$package" --no-cache-dir
    print_status "Installed $package"
done

# Phase 3: Project Structure Creation
echo -e "${PURPLE}📁 Phase 3: Project Structure Setup${NC}"
echo "----------------------------------------"

# Create main project directory
PROJECT_DIR="$HOME/storage/shared/the_new_civilization"
mkdir -p "$PROJECT_DIR"
print_status "Created main project directory: $PROJECT_DIR"

# Create subdirectories
DIRECTORIES=(
    "scripts"
    "config"
    "data" # For local data, e.g., prompt files
    "logs"
    "business" # For business scripts/data if any
    "interfaces" # For any local lightweight interfaces (e.g., CLI)
)

for dir in "${DIRECTORIES[@]}"; do
    mkdir -p "$PROJECT_DIR/$dir"
    print_status "Created directory: $dir"
done

# Phase 4: Configuration Files
echo -e "${PURPLE}⚙️ Phase 4: Configuration Setup${NC}"
echo "----------------------------------------"

# Create environment configuration template
cat > "$PROJECT_DIR/config/.env.template" << 'EOF'
# Hugging Face Configuration
# Get your token from https://huggingface.co/settings/tokens
HF_TOKEN=your_hugging_face_token_here
HF_USERNAME=your_hugging_face_username_here

# API Configuration (Optional, for other services)
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

# Business Configuration (Optional)
BUSINESS_EMAIL=your_business_email@example.com
WEBHOOK_URL=
EOF
print_status "Environment template created: config/.env.template"

# Create the actual .env file for the user to edit
cp "$PROJECT_DIR/config/.env.template" "$PROJECT_DIR/config/.env"
print_warning "Please edit '$PROJECT_DIR/config/.env' with your Hugging Face Token and Username!"

# Create main configuration file (Python based, for default models and settings)
cat > "$PROJECT_DIR/config/civilization_config.py" << 'EOF'
"""
The New Civilization - Main Configuration (Ultra-Lightweight API-First)
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CivilizationConfig:
    """Main configuration class for The New Civilization"""

    # Project paths
    BASE_DIR = Path.home() / "storage" / "shared" / "the_new_civilization"
    SCRIPTS_DIR = BASE_DIR / "scripts"
    DATA_DIR = BASE_DIR / "data"
    LOGS_DIR = BASE_DIR / "logs"
    CONFIG_DIR = BASE_DIR / "config"

    # Hugging Face API configuration
    HF_TOKEN = os.getenv("HF_TOKEN")
    HF_USERNAME = os.getenv("HF_USERNAME")
    # Base URL for Hugging Face Inference API
    HF_INFERENCE_API_BASE = "https://api-inference.huggingface.co/models/"

    # Default models for various tasks (to be called via API)
    # These are just model IDs, the models themselves run on HF's infrastructure
    DEFAULT_API_MODELS = {
        "text-generation": "microsoft/DialoGPT-medium",
        "text-classification": "cardiffnlp/twitter-roberta-base-sentiment-latest",
        "summarization": "facebook/bart-large-cnn",
        "translation_en_to_id": "Helsinki-NLP/opus-mt-en-id", # Example for English to Indonesian
        "image-generation": "runwayml/stable-diffusion-v1-5",
        "speech-to-text": "openai/whisper-base"
    }

    # API Request Timeout
    API_TIMEOUT = 60 # seconds

# Initialize configuration
config = CivilizationConfig()
EOF
print_status "Main Python configuration created: config/civilization_config.py"

# Phase 5: Create API Orchestrator Script
echo -e "${PURPLE}🚀 Phase 5: Create API Orchestrator Script${NC}"
echo "-------------------------------------------------"

# Save the API Orchestrator script to scripts/civilization_hf_orchestrator.py
cat > "$PROJECT_DIR/scripts/civilization_hf_orchestrator.py" << 'EOF'
#!/usr/bin/env python3
"""
THE NEW CIVILIZATION - Hugging Face API Orchestrator (ULTRA-LIGHTWEIGHT)
Main orchestration system for coordinating all AI operations via Hugging Face Inference API.

This script functions as a pure command center, sending requests to and receiving
responses from Hugging Face's hosted models, without local heavy dependencies.
"""

import os
import sys
import json
import time
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from enum import Enum

import requests
from huggingface_hub import HfApi, login
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.text import Text

# Configuration
# Adjust sys.path to ensure config.py is found
sys.path.insert(0, str(Path.home() / "storage" / "shared" / "the_new_civilization" / "config"))
try:
    from civilization_config import config
except ImportError:
    print("❌ Configuration not found! Please ensure 'civilization_config.py' is in the config directory and run the setup script.")
    sys.exit(1)

console = Console()

class TaskType(Enum):
    """Supported AI task types for Hugging Face Inference API"""
    TEXT_GENERATION = "text-generation"
    TEXT_CLASSIFICATION = "text-classification"
    SUMMARIZATION = "summarization"
    TRANSLATION = "translation_en_to_id" # Example: English to Indonesian
    QUESTION_ANSWERING = "question-answering"
    IMAGE_GENERATION = "image-generation" # Text-to-Image
    SPEECH_TO_TEXT = "speech-to-text"

class CivilizationApiOrchestrator:
    """Main orchestration system for The New Civilization using Hugging Face Inference API"""

    def __init__(self):
        """Initialize the orchestrator"""
        self.console = console
        self.hf_api = HfApi() # Used for Hub interaction like listing models
        self.processing_stats = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "api_cost_estimate": 0.0 # A very rough estimate, HF API usually charges per request/compute time
        }
        self.logger = self._setup_logging()
        self._authenticate()
        self.logger.info("🚀 Civilization API Orchestrator initialized (Ultra-Lightweight)")
        self.logger.info(f"Hugging Face Inference API Base: {config.HF_INFERENCE_API_BASE}")

    def _setup_logging(self):
        """Setup logging system"""
        log_dir = config.LOGS_DIR
        log_dir.mkdir(exist_ok=True)

        logger = logging.getLogger("CivilizationApiOrchestrator")
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_dir / "orchestrator_api.log")
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logger.addHandler(stream_handler)
        return logger

    def _authenticate(self):
        """Authenticate with Hugging Face Hub for API token validation"""
        if config.HF_TOKEN:
            try:
                # This login is for the huggingface_hub library, primarily for Hub interaction.
                # The actual Inference API calls use the token directly in headers.
                login(token=config.HF_TOKEN, add_to_git_credential=False)
                self.logger.info("✅ Authenticated with Hugging Face Hub")
            except Exception as e:
                self.logger.error(f"❌ Hugging Face Hub authentication failed: {e}")
        else:
            self.logger.warning("⚠️ No HF_TOKEN found - Hugging Face API calls might fail or be rate-limited.")

    def query_hf_inference_api(self, model_id: str, payload: Dict[str, Any], task: str) -> Dict[str, Any]:
        """
        Sends a query to the Hugging Face Inference API.
        Assumes the model_id is a valid model hosted on Hugging Face.
        """
        if not config.HF_TOKEN:
            raise ValueError("HF_TOKEN is required to query Hugging Face Inference API.")

        api_url = f"{config.HF_INFERENCE_API_BASE}{model_id}"
        headers = {"Authorization": f"Bearer {config.HF_TOKEN}"}

        self.logger.info(f"➡️ Querying HF Inference API for {task} using model: {model_id}")

        response = requests.post(api_url, headers=headers, json=payload, timeout=config.API_TIMEOUT)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()

    def process_ai_request(self, task_type: TaskType, input_data: Any, model_name: Optional[str] = None, parameters: Optional[Dict] = None) -> Dict[str, Any]:
        """Process a single AI request using Hugging Face Inference API."""
        self.processing_stats["total_requests"] += 1
        start_time = time.time()
        result = {}

        # Determine the model to use
        current_model = model_name or config.DEFAULT_API_MODELS.get(task_type.value)
        if not current_model:
            self.logger.error(f"❌ No model specified or default model found for task: {task_type.value}")
            self.processing_stats["failed_requests"] += 1
            return {"status": "error", "error": "No model found for task."}

        try:
            payload = {"inputs": input_data}
            if parameters:
                payload["parameters"] = parameters

            if task_type == TaskType.TEXT_GENERATION:
                api_result = self.query_hf_inference_api(current_model, payload, "text-generation")
                result = {"generated_text": api_result[0].get('generated_text')}
            elif task_type == TaskType.TEXT_CLASSIFICATION:
                api_result = self.query_hf_inference_api(current_model, payload, "text-classification")
                # api_result is a list of lists: [[{'label': 'LABEL_1', 'score': 0.99}, ...]]
                result = {"classification": api_result[0]}
            elif task_type == TaskType.SUMMARIZATION:
                api_result = self.query_hf_inference_api(current_model, payload, "summarization")
                result = {"summary_text": api_result[0].get('summary_text')}
            elif task_type == TaskType.TRANSLATION:
                api_result = self.query_hf_inference_api(current_model, payload, "translation")
                result = {"translation_text": api_result[0].get('translation_text')}
            elif task_type == TaskType.IMAGE_GENERATION:
                # Image generation returns raw bytes. We'll save it locally.
                # For this, we'll need a slightly different request as it returns bytes, not JSON.
                # This requires direct requests.post with stream=True and content parsing.
                # For simplicity in this example, we'll simulate or instruct on saving.
                self.logger.info(f"🖼️ Requesting image for: '{input_data}' from {current_model}")
                # The HF Inference API for image-generation returns image bytes directly.
                # We need to handle this as a binary response.
                image_response = requests.post(api_url := f"{config.HF_INFERENCE_API_BASE}{current_model}",
                                               headers=headers,
                                               json={"inputs": input_data},
                                               timeout=config.API_TIMEOUT)
                image_response.raise_for_status()

                image_dir = config.DATA_DIR / "generated_images"
                image_dir.mkdir(exist_ok=True)
                image_filename = image_dir / f"image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

                with open(image_filename, "wb") as f:
                    f.write(image_response.content)

                result = {"image_path": str(image_filename), "message": "Image saved locally."}
                self.logger.info(f"✅ Image saved to: {image_filename}")

            else:
                raise ValueError(f"Unsupported task type for API: {task_type.value}")

            processing_time = time.time() - start_time
            # Cost estimation is very rough; actual costs depend on HF's pricing.
            cost_estimate = processing_time * 0.001 + 0.01 # Example: $0.01 base + $0.001 per second
            self.processing_stats["api_cost_estimate"] += cost_estimate
            self.processing_stats["successful_requests"] += 1

            self.logger.info(f"✅ Request processed in {processing_time:.2f}s - Est. Cost: ${cost_estimate:.4f}")
            return {
                "status": "success",
                "result": result,
                "processing_time": processing_time,
                "estimated_cost": cost_estimate,
                "model_used": current_model,
                "timestamp": datetime.now().isoformat()
            }

        except requests.exceptions.RequestException as req_err:
            self.logger.error(f"❌ API request failed: {req_err}")
            self.processing_stats["failed_requests"] += 1
            return {"status": "error", "error": f"API request error: {req_err}"}
        except ValueError as ve:
            self.logger.error(f"❌ Configuration/Value error: {ve}")
            self.processing_stats["failed_requests"] += 1
            return {"status": "error", "error": f"Configuration error: {ve}"}
        except Exception as e:
            self.processing_stats["failed_requests"] += 1
            self.logger.error(f"❌ An unexpected error occurred: {e}")
            return {"status": "error", "error": str(e)}

    def display_status(self):
        """Display current system status and processing stats."""
        table = Table(title="🚀 The New Civilization - API Orchestrator Status")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Total Requests", str(self.processing_stats["total_requests"]))
        table.add_row("Successful", str(self.processing_stats["successful_requests"]))
        table.add_row("Failed", str(self.processing_stats["failed_requests"]))
        table.add_row("Est. API Cost", f"${self.processing_stats['api_cost_estimate']:.4f}")

        total = self.processing_stats["total_requests"]
        success_rate = (self.processing_stats["successful_requests"] / total * 100) if total > 0 else 0
        table.add_row("Success Rate", f"{success_rate:.1f}%")

        self.console.print(table)

    def start_interactive_mode(self):
        """Start interactive mode for testing API calls."""
        self.console.print(Panel(
            "🚀 [bold magenta]THE NEW CIVILIZATION[/bold magenta]\n"
            "Interactive API Orchestrator (Ultra-Lightweight)\n\n"
            "Available commands:\n"
            "• [cyan]textgen[/cyan] - Text Generation\n"
            "• [cyan]classify[/cyan] - Text Classification\n"
            "• [cyan]summarize[/cyan] - Text Summarization\n"
            "• [cyan]translate[/cyan] - Translate (EN->ID)\n"
            "• [cyan]imagegen[/cyan] - Image Generation (Text-to-Image)\n"
            "• [cyan]status[/cyan] - Show system status\n"
            "• [cyan]quit[/cyan] - Exit",
            title="Interactive API Mode",
            border_style="green"
        ))

        while True:
            try:
                command = self.console.input("\n[bold cyan]Enter command:[/bold cyan] ").strip().lower()

                if command == "quit":
                    break
                elif command == "status":
                    self.display_status()
                elif command == "textgen":
                    self._handle_text_generation()
                elif command == "classify":
                    self._handle_text_classification()
                elif command == "summarize":
                    self._handle_summarization()
                elif command == "translate":
                    self._handle_translation()
                elif command == "imagegen":
                    self._handle_image_generation()
                else:
                    self.console.print("[red]Unknown command. Type 'quit' to exit.[/red]")

            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted by user[/yellow]")
                break
            except Exception as e:
                self.console.print(f"[red]Error in interactive mode: {e}[/red]")
                self.logger.error(f"Error in interactive mode: {e}")

    def _handle_text_generation(self):
        """Handle text generation request."""
        prompt = self.console.input("Enter prompt for text generation: ")
        if prompt.strip():
            # Example parameters for text generation
            params = {"max_new_tokens": 100, "return_full_text": False}
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=self.console) as progress:
                task = progress.add_task("[cyan]Generating text...", total=1)
                result = self.process_ai_request(TaskType.TEXT_GENERATION, prompt, parameters=params)
                progress.update(task, completed=1)

            if result["status"] == "success":
                self.console.print(f"\n[green]Generated Text:[/green] {result['result']['generated_text']}")
            else:
                self.console.print(f"[red]Error: {result['error']}[/red]")

    def _handle_text_classification(self):
        """Handle text classification request."""
        text = self.console.input("Enter text to classify: ")
        if text.strip():
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=self.console) as progress:
                task = progress.add_task("[cyan]Classifying text...", total=1)
                result = self.process_ai_request(TaskType.TEXT_CLASSIFICATION, text)
                progress.update(task, completed=1)

            if result["status"] == "success":
                self.console.print("\n[green]Classification Results:[/green]")
                for item in result['result']['classification']:
                    self.console.print(f"  - Label: [bold blue]{item['label']}[/bold blue], Score: [yellow]{item['score']:.4f}[/yellow]")
            else:
                self.console.print(f"[red]Error: {result['error']}[/red]")

    def _handle_summarization(self):
        """Handle text summarization request."""
        text = self.console.input("Enter text to summarize: ")
        if text.strip():
            # Example parameters for summarization
            params = {"min_length": 30, "max_length": 150}
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=self.console) as progress:
                task = progress.add_task("[cyan]Summarizing text...", total=1)
                result = self.process_ai_request(TaskType.SUMMARIZATION, text, parameters=params)
                progress.update(task, completed=1)

            if result["status"] == "success":
                self.console.print(f"\n[green]Summary:[/green] {result['result']['summary_text']}")
            else:
                self.console.print(f"[red]Error: {result['error']}[/red]")

    def _handle_translation(self):
        """Handle translation request (English to Indonesian)."""
        text = self.console.input("Enter text to translate (EN->ID): ")
        if text.strip():
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=self.console) as progress:
                task = progress.add_task("[cyan]Translating text...", total=1)
                result = self.process_ai_request(TaskType.TRANSLATION, text)
                progress.update(task, completed=1)

            if result["status"] == "success":
                self.console.print(f"\n[green]Translation (ID):[/green] {result['result']['translation_text']}")
            else:
                self.console.print(f"[red]Error: {result['error']}[/red]")

    def _handle_image_generation(self):
        """Handle image generation request (Text-to-Image)."""
        prompt = self.console.input("Enter prompt for image generation: ")
        if prompt.strip():
            with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), BarColumn(), TaskProgressColumn(), console=self.console) as progress:
                task = progress.add_task("[cyan]Generating image...", total=1)
                result = self.process_ai_request(TaskType.IMAGE_GENERATION, prompt)
                progress.update(task, completed=1)

            if result["status"] == "success":
                self.console.print(f"\n[green]Image generated and saved to:[/green] [bold underline]{result['result']['image_path']}[/bold underline]")
                self.console.print("You can view the image using a file manager or image viewer.")
            else:
                self.console.print(f"[red]Error: {result['error']}[/red]")

def main():
    """Main entry point for the API orchestrator."""
    orchestrator = CivilizationApiOrchestrator()

    console.print(Panel(
        "🚀 [bold magenta]THE NEW CIVILIZATION[/bold magenta] 🚀\n\n"
        "✨ [bold green]Hugging Face API Orchestrator Online[/bold green]\n"
        "🧠 Powered by 100,000+ Models via API\n"
        "📱 Ultra-Lightweight Command Center on Mobile\n"
        "⚡ API-First & Cloud-Native",
        title="System Initialized",
        border_style="green"
    ))

    # Start interactive mode
    orchestrator.start_interactive_mode()

    # Show final stats
    console.print("\n[yellow]Session Summary:[/yellow]")
    orchestrator.display_status()

    console.print("\n[green]Thank you for using The New Civilization API Orchestrator! 🚀[/green]")

if __name__ == "__main__":
    main()
EOF
print_status "API Orchestrator script created: scripts/civilization_hf_orchestrator.py"
print_info "Ensuring script is executable..."
chmod +x "$PROJECT_DIR/scripts/civilization_hf_orchestrator.py"

# Phase 6: Quick Start Script
echo -e "${PURPLE}⚡ Phase 6: Quick Start Script${NC}"
echo "------------------------------"

# Create a simplified quick_start.py
cat > "$PROJECT_DIR/quick_start.py" << 'EOF'
#!/usr/bin/env python3
"""
THE NEW CIVILIZATION - Quick Start Script (Ultra-Lightweight)
Launch your AI civilization's command center.
"""

import os
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def main():
    """Main quick start function"""

    title = Text("🚀 THE NEW CIVILIZATION 🚀", style="bold magenta")
    subtitle = Text("Hugging Face API-Powered AI Revolution (Ultra-Lightweight)", style="cyan")

    welcome_panel = Panel(
        f"{title}\n{subtitle}\n\n"
        "✨ Ultra-lightweight AI/ML/DL platform\n"
        "🧠 100,000+ Hugging Face models via API\n"
        "📱 Optimized for mobile as pure command center",
        title="Welcome",
        border_style="green"
    )

    console.print(welcome_panel)

    config_path = Path.home() / "storage" / "shared" / "the_new_civilization" / "config" / ".env"

    if not config_path.exists():
        console.print("\n⚠️ [yellow]Configuration file (.env) not found![/yellow]")
        console.print("Please create and edit it from '.env.template' with your Hugging Face Token and Username.")
        console.print(f"Edit: [bold green]{config_path}[/bold green]")
        return
    
    # Check if HF_TOKEN is actually set in .env
    from dotenv import load_dotenv
    load_dotenv(config_path) # Load from the specific path
    if not os.getenv("HF_TOKEN") or "your_hugging_face_token_here" in os.getenv("HF_TOKEN"):
        console.print("\n⚠️ [yellow]HF_TOKEN not configured in .env![/yellow]")
        console.print("Please open and edit the .env file to add your Hugging Face API token.")
        console.print(f"Edit: [bold green]{config_path}[/bold green]")
        return


    console.print("\n✅ [green]Environment ready![/green]")
    console.print("\n🚀 [bold red]To start the API Orchestrator, run:[/bold red]")
    console.print(f"   [bold yellow]python {Path.home()}/storage/shared/the_new_civilization/scripts/civilization_hf_orchestrator.py[/bold yellow]")
    console.print("\n[dim]Make sure your .env file in 'config/' contains your Hugging Face Token.[/dim]")

if __name__ == "__main__":
    main()
EOF
print_status "Quick start script created: quick_start.py"
print_info "Ensuring script is executable..."
chmod +x "$PROJECT_DIR/quick_start.py"

# Final message
echo -e "${PURPLE}🎉 THE NEW CIVILIZATION (ULTRA-LIGHTWEIGHT) SETUP COMPLETE!${NC}"
echo "================================================================"
echo ""
echo -e "${GREEN}✅ Next IMPORTANT STEPS:${NC}"
echo "1. Go to your project directory: ${BLUE}cd $PROJECT_DIR${NC}"
echo "2. ${RED}EDIT YOUR HUGGING FACE TOKEN & USERNAME:${NC}"
echo "   Open ${BLUE}$PROJECT_DIR/config/.env${NC} using nano or vim and replace 'your_hugging_face_token_here' and 'your_hugging_face_username_here' with your actual Hugging Face API Token and Username."
echo "   (Get your token from: https://huggingface.co/settings/tokens)"
echo "3. Run the quick start script: ${BLUE}python quick_start.py${NC}"
echo "4. In the next step, I will provide the main Python orchestrator script!"
echo ""
echo -e "${RED}🚀 Ready to revolutionize the world with AI from your mobile!${NC}"