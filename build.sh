#!/bin/bash

# Create a virtual environment
python3.12 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
python3.12 -m pip install -r requirements.txt

# Set the FLASK_APP environment variable and run the Flask app
export FLASK_APP=main/main.py
flask run

# Deactivate the virtual environment
deactivate

rm -rf venv