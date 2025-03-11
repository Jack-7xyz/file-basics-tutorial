#!/usr/bin/env python3

"""Main entry point for the application.

This file demonstrates proper Python file structure and imports.
"""

import os
import json
from helpers.file_handler import read_config

def main():
    # Example of working with different file types
    config = read_config('../config/settings.json')
    print('Configuration loaded successfully!')

if __name__ == '__main__':
    main()