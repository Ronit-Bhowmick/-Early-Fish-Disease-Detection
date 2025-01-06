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