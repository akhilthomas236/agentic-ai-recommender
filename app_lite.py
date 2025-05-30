import streamlit as st
import json
from src.data.frameworks_data import (
    AGENT_FRAMEWORKS,
    RAG_FRAMEWORKS,
    QA_FRAMEWORKS,
    INTEGRATION_FRAMEWORKS
)

# Page configuration
st.set_page_config(
    page_title="AI Agentic Tool Recommender (Lite)",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply simple CSS
st.markdown("""
<style>
.main {
    padding: 1rem;
}
.framework-card {
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 1rem;
    margin-bottom: 1rem;
}
.header-image {
    width: 80px;
}
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
with col2:
    st.title("AI Agentic Tool Recommender (Lite Version)")
    st.write("Find the best tools for building your AI agent applications")

# Sidebar
with st.sidebar:
    st.write("## Navigation")
    selected_tab = st.radio("", ["Framework Explorer", "About"], index=0)
    
    st.write("---")
    st.write("### Framework Categories")
    st.write("- **Agent Frameworks**: CrewAI, LangGraph, Haystack, Autogen, etc.")
    st.write("- **RAG Solutions**: Neo4j, pgVector, MongoDB Atlas, etc.")
    st.write("- **Quality & Observability**: RAGAS, Guardrails AI, etc.")
    st.write("- **Integration**: MCP, Google A2A, ANP, etc.")

# Main content
if selected_tab == "Framework Explorer":
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
    
    # Display as cards
    for framework in frameworks:
        st.markdown(f"""
        <div class="framework-card">
            <h4>{framework['name']}</h4>
            <p>{framework['description']}</p>
            <p><strong>Key Features:</strong></p>
            <ul>
                {"".join([f"<li>{feature}</li>" for feature in framework['key_features']])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add links if available
        if 'github' in framework:
            st.markdown(f"[GitHub Repository]({framework['github']})")
        
        if 'docs' in framework:
            st.markdown(f"[Documentation]({framework['docs']})")
        
        st.write("---")

elif selected_tab == "About":
    st.write("## ℹ️ About AI Agentic Tool Recommender")
    st.write("""
    This is the lite version of the AI Agentic Tool Recommender application, which helps you
    navigate the complex ecosystem of AI agent frameworks, RAG solutions, 
    quality assurance tools, and integration protocols to build effective AI agent applications.
    
    ### Framework Categories
    
    - **Agent Frameworks**: Tools like CrewAI, LangGraph, Haystack, Autogen, and Microsoft Semantic Kernel
    - **RAG & Vector DB Solutions**: Neo4j, pgvector, MongoDB Atlas, Elasticsearch, and more
    - **Quality & Observability**: RAGAS, Dynatrace, Guardrails AI, Traceloop, OpenLLMetry
    - **Integration & Interoperability**: MCP, Google A2A, BeeAI, Agent Network Protocol
    
    ### Note
    
    This lite version provides browsing capabilities without the recommendation engine to reduce dependencies.
    For the full version with project-based recommendations, please use the main application.
    """)

# Footer
st.markdown("---")
st.markdown("© 2025 AI Agentic Tool Recommender | Built with Streamlit (Lite Version)")
