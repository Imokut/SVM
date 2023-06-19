#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:23:48 2023

@author: ngota
"""

# create the .kaggle directory and an empty kaggle.json file

import os
import json
import subprocess
import logging
import zipfile


def make_kaggle_json(kaggle_username: str, kaggle_key: str):
    """Make a Kaggle.json file in root directory
    
    Args:
        kaggle_username (str): username in Kaggle.Json file
        kaggle_key (str): key in Kaggle.json file
    """
    # Get the user's root directory
    root_directory = os.path.expanduser('~')
    
    # Create the directory path
    directory_path = os.path.join(root_directory, '.kaggle')
    
    # Create the directory
    os.makedirs(directory_path, exist_ok=True)
    
    # Create the file path (kaggle.json)
    file_path = os.path.join(directory_path, 'kaggle.json')
    
    # Create the file
    open(file_path, 'a').close()
    
    # Set file permissions
    os.chmod(file_path, 0o600)

    # Save API token the kaggle.json file
    with open(file_path, "w+") as f:
        f.write(json.dumps({"username": kaggle_username, "key": kaggle_key}))


def load_kaggle_dataset(dataset_name:str) -> str:
    """Use kaggle command to load Kaggle dataset

    Args:
        dataset_name (str): Kaggle name for the dataset

    Returns:
        filepath (str): Path to the downloaded dataset

    """
    command = f'kaggle datasets download -d {dataset_name}'
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)  # Set the log level to ERROR or higher

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)  # Set the log level for console handler

    formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    try:
        subprocess.run(command, shell=True, check=True)
        return str(os.getcwd())
    
    except subprocess.CalledProcessError as e:
        logger.error(f'An error occurred while downloading the dataset: {e}')
        return None


def extract_zip(filepath:str):
    """Extract from zip to folder
    
    Args:
        filepath (str): Path to the zip file
    """    

    if filepath.endswith('.zip'):
        folder_name = os.path.splitext(os.path.basename(filepath))[0]
        os.makedirs(folder_name, exist_ok=True)

        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(folder_name)
            
        # Delete the zip file
        os.remove(filepath)
    
    else:
        print('Failed')
        
if __name__=="__main__":
    kaggle_username = "josephngotachilo"
    kaggle_key = "cbc282983c1363ecfbf2fd98ce9fac62"
    make_kaggle_json(kaggle_username, kaggle_key)
