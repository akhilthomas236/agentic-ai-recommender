"""
Application configuration settings
"""

# Application metadata
APP_NAME = "AI Agentic Tool Recommender"
VERSION = "1.0.0"
AUTHOR = "AI Developer"
COPYRIGHT_YEAR = "2025"

# UI settings
PRIMARY_COLOR = "#1E3A8A"
SECONDARY_COLOR = "#4B89DC"
MAX_RECOMMENDATIONS_PER_CATEGORY = 2  # Number of tools to recommend per category

# Recommendation engine settings
SIMILARITY_WEIGHT = 0.6  # Weight of text matching in recommendation score
PREFERENCE_WEIGHT = 0.4  # Weight of preference matching in recommendation score

# Default preferences (1-10 scale)
DEFAULT_PREFERENCES = {
    "scalability": 5,
    "performance": 5,
    "ease_of_integration": 5,
    "time_to_market": 5,
    "cost_effectiveness": 5,
    "customizability": 5,
}

# Category labels
CATEGORIES = {
    "agent_frameworks": "Agent Framework",
    "rag_vector_db": "RAG & Vector DB",
    "qa_observability": "Quality & Observability",
    "integration_interop": "Integration & Interoperability"
}
