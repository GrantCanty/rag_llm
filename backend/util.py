import logging
from pathlib import Path
import os


logger = logging.getLogger(__name__)

def get_available_text_and_files():
    available_text_files = {}
    s = Path('./backend/documents')
    for root, _, files in s.walk():
        for file in files:
            path = Path(file.lower())
            if path.suffix == ".txt":
                file_path = Path(root, file)
                f = open(file_path)
                available_text_files[file] = f.read()
                f.close()
    

    return available_text_files

def get_available_text_files():
    available_text_files = []
    s = Path('./backend/documents')
    for _, _, files in s.walk():
        for file in files:
            path = Path(file.lower())
            if path.suffix == ".txt":
                available_text_files.append(file)
    

    return available_text_files