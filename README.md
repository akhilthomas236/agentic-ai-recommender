# AI Agentic Tool Recommender

A Streamlit application that helps users navigate the complex ecosystem of AI agent development by recommending tools and frameworks based on project requirements.

🚀 **Live Demo**: [https://agentic-ai-recommender.streamlit.app/](https://agentic-ai-recommender.streamlit.app/)

## Features

- **Tool Recommendation Engine**: Get personalized recommendations for AI frameworks and tools based on your project description and preferences
- **Framework Explorer**: Browse and learn about various AI frameworks across different categories
- **Interactive UI**: User-friendly interface with sliders for setting preferences and interactive visualizations
- **Exportable Results**: Save your recommendations for future reference

## Categories of Tools

The application provides recommendations across four key categories:

1. **Agent Frameworks**: CrewAI, LangGraph, Haystack, Autogen, Microsoft Semantic Kernel
2. **RAG & Vector DB Solutions**: Neo4j, pgVector, MongoDB Atlas, Elasticsearch
3. **Quality & Observability**: RAGAS, Dynatrace, Guardrails AI, Traceloop, OpenLLMetry
4. **Integration & Interoperability**: MCP, Google A2A, BeeAI, Agent Network Protocol

## Installation

```bash
# Clone the repository
git clone https://github.com/akhilthomas236/agentic-ai-recommender.git
cd agentic-ai-recommender

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Note:** The application only requires a few core packages (streamlit, pandas, scikit-learn, plotly) to run. The full list of AI frameworks mentioned in the application are not actually imported or used in the code - they are only referenced in the data for recommendation purposes.

## Usage

```bash
# Method 1: Using the convenience script (recommended)
./run_app.sh
# This script will automatically fall back to a lite version 
# if there are issues installing all dependencies

# Method 2: Manual setup
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the full Streamlit app
streamlit run app.py

# OR run the lite version with minimal dependencies
streamlit run app_lite.py
```

This will start the application on your local machine and open it in your default web browser.

### Online Demo

The application is deployed and available online at:
[https://agentic-ai-recommender.streamlit.app/](https://agentic-ai-recommender.streamlit.app/)

You can access it directly from any web browser without installing anything locally.

### Python 3.13+ Compatibility

If you're using Python 3.13 or newer (where `distutils` has been removed), you may encounter dependency installation issues. The script will automatically handle this by falling back to the lite version, or you can manually run the lite version which requires only Streamlit.

## Project Structure

```
agentic-ai-recommender/
│
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
│
├── src/
│   ├── components/           # UI components
│   │   ├── styles.css        # Custom CSS styles
│   │   └── ui_components.py  # Reusable UI components
│   │
│   ├── data/                 # Data definitions
│   │   └── frameworks_data.py  # Framework information
│   │
│   └── utils/                # Utility functions
│       └── tool_recommendation.py  # Tool recommendation logic
│
└── README.md                 # Project documentation
```

## Development

To add more frameworks or tools to the recommendation system:

1. Update the corresponding list in `src/data/frameworks_data.py`
2. Ensure you include all required fields: name, description, key_features, and scoring metrics
3. The recommendation engine will automatically incorporate new entries

## License

MIT

## Acknowledgments

- This project was created to help developers navigate the growing ecosystem of AI agent development tools.
- Framework information is collected from official documentation, GitHub repositories, and community resources.
