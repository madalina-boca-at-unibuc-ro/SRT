#!/home/madalina/soft/py_env/bin/python3
"""
Launcher script for the SRT (Special Relativity Theory) simulator.
This script ensures the src directory is in the Python path and launches the application.
"""

import sys
import os

# Add the src directory to the Python path
src_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.insert(0, src_path)

# Change to the src directory so relative paths work correctly
os.chdir(src_path)

# Import and run the main application
from main import app

if __name__ == "__main__":
    app.run()
