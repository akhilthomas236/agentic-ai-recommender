import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from src.data.frameworks_data import (
    AGENT_FRAMEWORKS,
    RAG_FRAMEWORKS,
    QA_FRAMEWORKS,
    INTEGRATION_FRAMEWORKS
)

def preprocess_text(text):
    """Preprocess text for better matching"""
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^\w\s]', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def calculate_framework_scores(project_description, preferences, frameworks_list):
    """Calculate scores for frameworks based on text similarity and user preferences"""
    # Preprocess project description
    processed_description = preprocess_text(project_description)
    
    # Create corpus with project description and framework descriptions
    corpus = [processed_description]
    framework_descriptions = []
    
    for framework in frameworks_list:
        # Combine name, description and features for better matching
        combined_text = f"{framework['name']} {framework['description']} {' '.join(framework['key_features'])}"
        processed_text = preprocess_text(combined_text)
        corpus.append(processed_text)
        framework_descriptions.append(processed_text)
    
    # Calculate TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    
    # Calculate similarity between project description and each framework
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    
    # Adjust scores based on preferences
    adjusted_scores = []
    for i, framework in enumerate(frameworks_list):
        base_score = similarity_scores[i]
        
        # Apply preference weights
        # For each attribute (e.g., scalability), we:
        # 1. Get the user's preference (1-10) for that attribute
        # 2. Multiply it by the framework's rating (1-10) for that attribute
        # 3. Normalize by dividing by 10 to keep the scale consistent
        # This gives higher scores to frameworks that excel in areas the user cares about most
        preference_score = (
            (preferences['scalability'] * framework.get('scalability', 5) / 10) +
            (preferences['performance'] * framework.get('performance', 5) / 10) +
            (preferences['ease_of_integration'] * framework.get('ease_of_integration', 5) / 10) +
            (preferences['time_to_market'] * framework.get('time_to_market', 5) / 10) +
            (preferences['cost_effectiveness'] * framework.get('cost_effectiveness', 5) / 10) +
            (preferences['customizability'] * framework.get('customizability', 5) / 10)
        ) / 6  # Average weight across all attributes
        
        # Combined score (60% text similarity + 40% preference alignment)
        # Text similarity ensures functional relevance to the project description
        # Preference alignment ensures the tool matches user's priorities
        combined_score = 0.6 * base_score + 0.4 * (preference_score / 10)
        adjusted_scores.append(combined_score)
    
    return adjusted_scores

def recommend_tools(project_description, preferences):
    """
    Generate tool recommendations based on project description and preferences
    """
    recommendations = {}
    
    # Get scores for each framework type
    agent_scores = calculate_framework_scores(project_description, preferences, AGENT_FRAMEWORKS)
    rag_scores = calculate_framework_scores(project_description, preferences, RAG_FRAMEWORKS)
    qa_scores = calculate_framework_scores(project_description, preferences, QA_FRAMEWORKS)
    integration_scores = calculate_framework_scores(project_description, preferences, INTEGRATION_FRAMEWORKS)
    
    # Select top frameworks from each category
    recommendations["Agent Framework"] = [AGENT_FRAMEWORKS[i] for i in np.argsort(agent_scores)[-2:][::-1]]
    recommendations["RAG & Vector DB"] = [RAG_FRAMEWORKS[i] for i in np.argsort(rag_scores)[-2:][::-1]]
    recommendations["Quality & Observability"] = [QA_FRAMEWORKS[i] for i in np.argsort(qa_scores)[-2:][::-1]]
    recommendations["Integration & Interoperability"] = [INTEGRATION_FRAMEWORKS[i] for i in np.argsort(integration_scores)[-2:][::-1]]
    
    # Add score to each recommendation
    for category, frameworks in recommendations.items():
        if category == "Agent Framework":
            for i, framework in enumerate(frameworks):
                framework['score'] = agent_scores[AGENT_FRAMEWORKS.index(framework)]
        elif category == "RAG & Vector DB":
            for i, framework in enumerate(frameworks):
                framework['score'] = rag_scores[RAG_FRAMEWORKS.index(framework)]
        elif category == "Quality & Observability":
            for i, framework in enumerate(frameworks):
                framework['score'] = qa_scores[QA_FRAMEWORKS.index(framework)]
        elif category == "Integration & Interoperability":
            for i, framework in enumerate(frameworks):
                framework['score'] = integration_scores[INTEGRATION_FRAMEWORKS.index(framework)]
    
    return recommendations
