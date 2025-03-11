"""Helper module for file operations.

This module demonstrates proper file handling in Python.
"""

import json
import yaml
from pathlib import Path

def read_config(file_path: str) -> dict:
    """Read a configuration file.
    
    Demonstrates:
    1. Path handling
    2. File extension checking
    3. Error handling
    4. Type hints
    """
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")
    
    if path.suffix == '.json':
        with open(path, 'r') as f:
            return json.load(f)
    elif path.suffix in ('.yml', '.yaml'):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    else:
        raise ValueError(f"Unsupported config file type: {path.suffix}")