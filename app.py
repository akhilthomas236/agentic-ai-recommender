import streamlit as st
import pandas as pd
import json
import os
from src.utils.tool_recommendation import recommend_tools
from src.components.ui_components import (
    render_header, 
    render_sidebar, 
    render_tool_cards,
    render_architecture_diagram
)
from src.data.frameworks_data import (
    AGENT_FRAMEWORKS,
    RAG_FRAMEWORKS,
    QA_FRAMEWORKS,
    INTEGRATION_FRAMEWORKS
)

# Page configuration
st.set_page_config(
    page_title="AI Agentic Tool Recommender",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
with open('src/components/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Header
render_header()

# Sidebar
selected_tab = render_sidebar()

# Main content
if selected_tab == "Tool Recommender":
    st.write("## 🔍 AI Agentic Tool Recommender")
    
    # User input for project idea
    project_description = st.text_area(
        "Describe your AI agentic project idea or use case:",
        height=150,
        placeholder="E.g., I want to build a conversational AI assistant that can research topics online, summarize documents, and answer questions using multiple data sources..."
    )
    
    # Feature preference selection
    st.write("### Select your feature preferences:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("#### Technical Priorities:")
        scalability = st.slider("Scalability", 1, 10, 5)
        performance = st.slider("Performance", 1, 10, 5)
        ease_of_integration = st.slider("Ease of Integration", 1, 10, 5)
    
    with col2:
        st.write("#### Business Priorities:")
        time_to_market = st.slider("Time to Market", 1, 10, 5)
        cost_effectiveness = st.slider("Cost Effectiveness", 1, 10, 5)
        customizability = st.slider("Customizability", 1, 10, 5)
    
    # Create a preferences dictionary
    preferences = {
        "scalability": scalability,
        "performance": performance,
        "ease_of_integration": ease_of_integration,
        "time_to_market": time_to_market,
        "cost_effectiveness": cost_effectiveness,
        "customizability": customizability,
    }
    
    # Generate recommendations
    if st.button("Generate Recommendations", type="primary"):
        if not project_description:
            st.error("Please describe your project idea first.")
        else:
            with st.spinner("Analyzing your project requirements and generating recommendations..."):
                # Get recommendations based on project description and preferences
                recommendations = recommend_tools(project_description, preferences)
                
                # Display recommendations
                st.success("✅ Analysis complete! Here are the recommended tools for your project:")
                
                st.write("## Recommended Architecture")
                
                # Display architecture diagram
                render_architecture_diagram(recommendations)
                
                # Display recommended tools by category
                for category, tools in recommendations.items():
                    st.write(f"### {category} Tools")
                    render_tool_cards(tools)
                
                # Export option
                st.download_button(
                    label="📥 Export Recommendations",
                    data=json.dumps(recommendations, indent=4),
                    file_name="ai_agent_recommendations.json",
                    mime="application/json",
                )

elif selected_tab == "Framework Explorer":
    st.write("## 🔎 AI Frameworks Explorer")
    
    # Framework categories
    framework_categories = {
        "Agent Frameworks": AGENT_FRAMEWORKS,
        "RAG & Vector DB Solutions": RAG_FRAMEWORKS,
        "Quality & Observability": QA_FRAMEWORKS,
        "Integration & Interoperability": INTEGRATION_FRAMEWORKS
    }
    
    # Category selection
    category = st.selectbox("Select Framework Category", list(framework_categories.keys()))
    
    # Display frameworks in the selected category
    st.write(f"### {category}")
    frameworks = framework_categories[category]
    
    # Display as expandable cards
    for i in range(0, len(frameworks), 3):
        cols = st.columns(3)
        for j in range(3):
            if i+j < len(frameworks):
                with cols[j]:
                    with st.expander(f"{frameworks[i+j]['name']}"):
                        st.write(f"**{frameworks[i+j]['name']}**")
                        st.write(frameworks[i+j]['description'])
                        st.write("**Key Features:**")
                        for feature in frameworks[i+j]['key_features']:
                            st.write(f"- {feature}")
                        
                        if 'github' in frameworks[i+j]:
                            st.markdown(f"[GitHub Repository]({frameworks[i+j]['github']})")
                        
                        if 'docs' in frameworks[i+j]:
                            st.markdown(f"[Documentation]({frameworks[i+j]['docs']})")

elif selected_tab == "About":
    st.write("## ℹ️ About AI Agentic Tool Recommender")
    st.write("""
    This application helps you navigate the complex ecosystem of AI agent frameworks, RAG solutions, 
    quality assurance tools, and integration protocols to build effective AI agent applications.
    
    ### How it Works
    
    1. **Describe your project idea** - Provide details about what you want to build
    2. **Set your preferences** - Adjust sliders to indicate your technical and business priorities
    3. **Get recommendations** - Receive tailored suggestions for tools in each category
    4. **Explore the recommended architecture** - See how different tools can work together
    5. **Export your results** - Save your recommendations for later reference
    
    ### Framework Categories
    
    - **Agent Frameworks**: Tools like CrewAI, LangGraph, Haystack, Autogen, and Microsoft Semantic Kernel
    - **RAG & Vector DB Solutions**: Neo4j, pgvector, MongoDB Atlas, Elasticsearch, and more
    - **Quality & Observability**: RAGAS, Dynatrace, Guardrails AI, Traceloop, OpenLLMetry
    - **Integration & Interoperability**: MCP, Google A2A, BeeAI, Agent Network Protocol
    
    ### Feedback
    
    This is a prototype application. We welcome your feedback and suggestions for improvement!
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 AI Agentic Tool Recommender | Built with Streamlit")
