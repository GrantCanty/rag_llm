import logging
from pathlib import Path


logger = logging.getLogger(__name__)

def get_available_text_files():
    available_text_files = []
    s = Path('./backend/documents')
    for _, _, files in s.walk():
        for file in files:
            path = Path(file.lower())
            if path.endswith(".txt"):
                available_text_files.append(path)
    

    return available_text_files