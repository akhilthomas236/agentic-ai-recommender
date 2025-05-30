#!/bin/bash

# This script helps set up and run the AI Agentic Tool Recommender application

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run initialization script
echo "Initializing application..."
python init.py

# Run the Streamlit app
echo "Starting Streamlit application..."
streamlit run app.py
