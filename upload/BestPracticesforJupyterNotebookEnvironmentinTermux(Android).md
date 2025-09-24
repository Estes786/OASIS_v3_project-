# Best Practices for Jupyter Notebook Environment in Termux (Android)

This document outlines best practices for setting up, maintaining, and optimizing a Jupyter Notebook environment within Termux on Android, especially for resource-intensive tasks like AI development. These practices aim to enhance stability, performance, and reproducibility.

## 1. Environment Setup and Management

### 1.1. Utilize Python Virtual Environments (`venv`)

**Problem:** Installing Python packages globally in Termux can lead to dependency conflicts between different projects. This makes projects difficult to manage and reproduce.

**Solution:** Always create and activate a Python virtual environment (`venv`) for each project. This isolates project-specific dependencies, ensuring a clean and reproducible development environment.

**Steps:**
1.  **Install `python-virtualenv` (if not already installed):**
    ```bash
    pkg install python-virtualenv
    ```
2.  **Navigate to your project directory:**
    ```bash
    cd ~/path/to/your/project
    ```
3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
    (You can replace `venv` with any name for your virtual environment, e.g., `my_project_env`)
4.  **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    (Your terminal prompt should change to indicate the active `venv`)
5.  **Install Jupyter and project dependencies within the `venv`:**
    ```bash
    pip install jupyter
    pip install -r requirements.txt
    ```
6.  **Deactivate the virtual environment when done:**
    ```bash
    deactivate
    ```

### 1.2. Automate Setup with Shell Scripts

**Problem:** Manually setting up the environment can be tedious and error-prone, especially after reinstallation or on a new device.

**Solution:** Create a shell script (e.g., `setup_environment.sh`) to automate the entire setup process, including Termux package installation, `venv` creation, and Python dependency installation.

**Example `setup_environment.sh`:**
```bash
#!/bin/bash

echo "Updating Termux packages..."
pkg update && pkg upgrade -y

echo "Installing essential Termux packages..."
pkg install python nodejs git clang python-virtualenv -y

echo "Setting up storage access..."
termux-setup-storage

PROJECT_DIR="$HOME/fmaa-bdi-agent"

echo "Creating project directory: $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

echo "Creating Python virtual environment..."
python -m venv venv
source venv/bin/activate

echo "Installing Jupyter and project dependencies..."
pip install jupyter

# Create a dummy requirements.txt if it doesn't exist for initial setup
if [ ! -f "requirements.txt" ]; then
    echo "# Add your project dependencies here, e.g.:" > requirements.txt
    echo "numpy" >> requirements.txt
    echo "pandas" >> requirements.txt
    echo "matplotlib" >> requirements.txt
    echo "aiohttp" >> requirements.txt
    echo "asyncio" >> requirements.txt
    echo "supabase" >> requirements.txt
    echo "qiskit" >> requirements.txt
    echo "pennylane" >> requirements.txt
fi

pip install -r requirements.txt

echo "Jupyter Notebook environment setup complete!"
echo "To activate your environment, run: source $PROJECT_DIR/venv/bin/activate"
echo "To start Jupyter Notebook, run: jupyter notebook --no-browser --port=8888"
```

## 2. Resource Management and Optimization

Running a Jupyter Notebook server, VNC, and potentially multiple Python processes on an Android device can be resource-intensive. Effective resource management is crucial for stability and performance.

### 2.1. Monitor System Resources

**Problem:** High CPU or RAM usage can lead to system slowdowns, crashes, or battery drain.

**Solution:** Regularly monitor CPU and RAM usage. Termux provides basic tools for this.

**Commands:**
*   `top` or `htop` (install `htop` with `pkg install htop` for a more user-friendly interface): Provides a dynamic real-time view of running processes.
*   `free -h`: Shows memory usage.
*   `df -h`: Shows disk space usage.

### 2.2. Manage Jupyter Kernels

**Problem:** Inactive Jupyter kernels consume RAM and CPU resources unnecessarily.

**Solution:** Always shut down kernels of notebooks that are no longer in use.

**Steps:**
1.  From the Jupyter Dashboard, go to the "Running" tab.
2.  Click the "Shutdown" button next to any inactive notebooks.

### 2.3. Optimize Python Code for Performance

**Problem:** Inefficient Python code, especially in AI/ML tasks, can quickly exhaust resources.

**Solution:** Write optimized code, leverage libraries designed for performance (e.g., NumPy for numerical operations, `asyncio` for concurrent I/O), and consider profiling your code.

**Tips:**
*   **Use `asyncio`:** For I/O-bound operations (like network requests to Vercel, Supabase, GitHub APIs), use `asyncio` to perform tasks concurrently, as seen in the `belief_manager.py` and `industrial_orchestrator.py` examples.
*   **Vectorization:** For numerical computations, use vectorized operations with NumPy instead of Python loops.
*   **Profiling:** Use Python's built-in `cProfile` module or Jupyter's magic commands (`%timeit`, `%%timeit`) to identify performance bottlenecks in your code.

### 2.4. Strategic Use of VNC

**Problem:** VNC can be resource-heavy, especially with high display resolutions or frequent screen updates.

**Solution:** Use VNC judiciously. Consider running Jupyter in `--no-browser` mode and accessing it from a browser on another device on the same network if possible, or use a lower resolution for the VNC session.

**Starting Jupyter without opening a browser:**
```bash
jupyter notebook --no-browser --port=8888
```
Then, open a web browser (e.g., on your phone, tablet, or another computer connected to the same network) and navigate to `http://<your_termux_ip>:8888` (you might need to find your Termux IP address using `ifconfig` or `ip addr`).

### 2.5. Battery Optimization

**Problem:** Continuous operation of Termux and Jupyter can drain the Android device's battery quickly.

**Solution:** Utilize Termux features for battery management and ensure critical operations are not interrupted.

**Tips:**
*   **`termux-wake-lock`:** Use this command to prevent the device from sleeping during long-running processes. Remember to release the wake lock when the task is complete.
    ```bash
    termux-wake-lock
    # Your long-running script
    termux-wake-unlock
    ```
*   **Monitor Battery:** Use `termux-battery-status` to check battery levels and plan long tasks accordingly.

## 3. Maintenance and Troubleshooting

### 3.1. Regular Updates

**Problem:** Outdated packages can lead to security vulnerabilities, bugs, and compatibility issues.

**Solution:** Regularly update Termux packages and Python dependencies.

**Commands:**
*   `pkg update && pkg upgrade -y` (for Termux packages)
*   `pip install --upgrade pip setuptools wheel` (for Python packaging tools)
*   `pip install --upgrade -r requirements.txt` (for project dependencies)

### 3.2. Backup Important Data

**Problem:** Data loss can occur due to device issues or accidental deletions.

**Solution:** Regularly back up your project files, notebooks, and any critical data.

**Tips:**
*   **Version Control:** Use Git and GitHub (as already implemented in the project) to manage your code and notebooks. Push changes frequently.
*   **Manual Backups:** Periodically copy your project directory to external storage or cloud services.

### 3.3. Common Troubleshooting Tips

*   **Jupyter Kernel Dead:** If a kernel dies, try restarting it from the Jupyter Notebook menu (`Kernel > Restart`). If it persists, check your code for errors or memory issues.
*   **`ModuleNotFoundError`:** Ensure your virtual environment is activated and all necessary packages are listed in `requirements.txt` and installed (`pip install -r requirements.txt`).
*   **VNC Connection Issues:** Check if the VNC server is running in Termux (`vncserver -list`). Ensure the port is not blocked and your VNC client settings are correct.
*   **Storage Permissions:** If you encounter issues reading/writing files, ensure Termux has storage permissions (`termux-setup-storage`).

By adhering to these best practices, the FMAA BDI Agent project can maintain a robust, efficient, and scalable development environment on Android via Termux, maximizing the potential of its zero-cost philosophy.

