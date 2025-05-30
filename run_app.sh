#!/bin/bash

# This script helps set up and run the AI Agentic Tool Recommender application

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Full dependency installation failed. Installing minimal dependencies for lite mode..."
    pip install streamlit
    
    # Run the lite version of the app
    echo "Starting Streamlit application (lite version)..."
    streamlit run app_lite.py
else
    # Run initialization script
    echo "Initializing application..."
    python init.py

    # Run the full Streamlit app
    echo "Starting Streamlit application..."
    streamlit run app.py
fi
