
"""
This script is designed to automatically create the necessary project structure 
for an MLOps-based machine learning project named 'early_fish_disease_detection'.
It will generate directories and files that are typically needed for a project, 
including Python packages, configuration files, and project metadata files.

The generated structure is useful for organizing the project in a modular way and 
provides an initial scaffold for further development and experimentation.

The script performs the following tasks:
1. Creates the necessary directories and files in the project structure.
2. Logs the creation process to provide feedback to the user.
"""
import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# set up a project directory
project_name = 'early_fish_disease_detection'

# set up the list of file
file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/config.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebooks/trial.ipynb",

    # React Native-related files and directories
    "frontend/package.json",
    "frontend/.gitignore",
    "frontend/app.json",
    "frontend/index.js",
    "frontend/App.js",
    "frontend/src/components/HelloWorld.js",
    "frontend/src/screens/HomeScreen.js",
    "frontend/src/assets/logo.png",  # Example image, can be empty initially
    "frontend/src/styles/style.js",
    "frontend/metro.config.js",  # React Native Metro bundler config
    "frontend/android/app/src/main/AndroidManifest.xml",  # Android app entry point
]


for file in file_list:
    path = Path(file)
    if path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        logging.info(f"Created file: {path}")
    else:
        path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {path}")