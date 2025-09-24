"""
THE NEW CIVILIZATION - Setup Configuration
Ultra-Lightweight AI Platform Package Setup
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="the-new-civilization",
    version="3.0.0",
    author="The New Civilization Community",
    author_email="contact@thenewcivilization.ai",
    description="Ultra-lightweight AI platform with mobile orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/the-new-civilization",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/the-new-civilization/issues",
        "Documentation": "https://github.com/yourusername/the-new-civilization/blob/main/API_DOCUMENTATION.md",
        "HuggingFace Space": "https://huggingface.co/spaces/yourusername/the-new-civilization",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "oasis-orchestrator=termux_orchestrator:main",
            "new-civilization=app:main",
        ],
    },
    keywords="ai, machine-learning, api, mobile, termux, huggingface, ultra-lightweight",
    include_package_data=True,
    zip_safe=False,
)