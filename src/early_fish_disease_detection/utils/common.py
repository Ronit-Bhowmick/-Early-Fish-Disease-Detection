import os
from box.exceptions import BoxValueError
import yaml
from early_fish_disease_detection import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    """
    Read a yaml file and return the content as a dictionary
    """
    try:
        with open(yaml_path, "r") as file:
            config = yaml.safe_load(file)
            logger.info(f'yaml file {yaml_path} read successfully')
            return ConfigBox(config)
    except BoxValueError:
        raise BoxValueError(f'Error reading yaml file {yaml_path}')
    except Exception as e:
        raise e

@ensure_annotations
def create_dir(dir_path: list, verbose=True):
    """
    Create a directory if it does not exist
    """
    for path in dir_path:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Directory {path} created successfully')

@ensure_annotations
def save_json(json_path: Path, data: dict):
    """
    Save a dictionary as a json file
    """
    with open(json_path, "w") as file:
        json.dump(data, file, indent=4)
        logger.info(f'json file {json_path} saved successfully')


def load_json(json_path: Path) -> ConfigBox:
    """
    Load a json file and return the content as a dictionary
    """
    with open(json_path, "r") as file:
        data = json.load(file)
        logger.info(f'json file {json_path} loaded successfully')
        return ConfigBox(data)
    
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save a binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'binary file {path} saved successfully')


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file
    """
    data = joblib.load(filename=path)
    logger.info(f'binary file {path} loaded successfully')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in KB
    """
    size = os.path.getsize(path)
    return f'{size / 1024} KB'

@ensure_annotations
def encodeImagetoBase64(croppedImgPath):
    with open(croppedImgPath, "rb") as img_file:
        return base64.b64encode(img_file.read())
    
@ensure_annotations
def decodeBase64toImage(base64String, imagePath):
    img_data = base64.b64decode(base64String)
    with open(imagePath, "wb") as img_file:
        img_file.write(img_data)
        img_file.close()