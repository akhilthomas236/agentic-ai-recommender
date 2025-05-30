import streamlit as st
import plotly.graph_objects as go

def render_header():
    """Render the application header"""
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    with col2:
        st.title("AI Agentic Tool Recommender")
        st.write("Find the best tools for building your AI agent applications")

def render_sidebar():
    """Render sidebar with navigation and filters"""
    with st.sidebar:
        st.write("## Navigation")
        tabs = ["Tool Recommender", "Framework Explorer", "About"]
        selected_tab = st.radio("", tabs, index=0)
        
        st.write("---")
        st.write("### Framework Categories")
        st.write("- **Agent Frameworks**: CrewAI, LangGraph, Haystack, Autogen, etc.")
        st.write("- **RAG Solutions**: Neo4j, pgVector, MongoDB Atlas, etc.")
        st.write("- **Quality & Observability**: RAGAS, Guardrails AI, etc.")
        st.write("- **Integration**: MCP, Google A2A, ANP, etc.")
        
    return selected_tab

def render_tool_cards(tools):
    """Render tool recommendation cards"""
    cols = st.columns(len(tools))
    
    for i, tool in enumerate(tools):
        with cols[i]:
            st.markdown(f"""
            <div style="border:1px solid #ddd; border-radius:5px; padding:15px; margin:10px 0;">
                <h4>{tool['name']}</h4>
                <div style="background-color:#f0f5ff; padding:5px; border-radius:3px; margin:5px 0;">
                    Match Score: {tool['score']*100:.1f}%
                </div>
                <p><small>{tool['description']}</small></p>
                <p><strong>Key Features:</strong></p>
                <ul>
                    {"".join([f"<li><small>{feature}</small></li>" for feature in tool['key_features'][:3]])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

def render_architecture_diagram(recommendations):
    """Render an architecture diagram showing how the recommended tools connect"""
    # Create figure
    fig = go.Figure()
    
    # Node positions
    positions = {
        "Agent Framework": (0, 0.5),
        "RAG & Vector DB": (0.33, 0.5),
        "Quality & Observability": (0.66, 0.5),
        "Integration & Interoperability": (1, 0.5),
    }
    
    # Draw nodes
    for category, pos in positions.items():
        tools = recommendations[category]
        
        # Main category node
        fig.add_trace(go.Scatter(
            x=[pos[0]],
            y=[pos[1]],
            mode="markers+text",
            marker=dict(size=30, color="#4B89DC"),
            text=[category],
            textposition="bottom center",
            hoverinfo="text",
            name=category
        ))
        
        # Tool nodes (slightly above the category)
        tool_positions = []
        for i, tool in enumerate(tools):
            tool_x = pos[0] - 0.05 + (i * 0.1)
            tool_y = pos[1] + 0.15
            tool_positions.append((tool_x, tool_y))
            
            fig.add_trace(go.Scatter(
                x=[tool_x],
                y=[tool_y],
                mode="markers+text",
                marker=dict(size=20, color="#5CB85C"),
                text=[tool['name']],
                textposition="top center",
                hoverinfo="text",
                name=tool['name']
            ))
            
            # Connect tool to category
            fig.add_trace(go.Scatter(
                x=[tool_x, pos[0]],
                y=[tool_y, pos[1]],
                mode="lines",
                line=dict(width=1, color="#AAA"),
                hoverinfo="none",
                showlegend=False
            ))
    
    # Connect categories with arrows
    for i in range(len(positions) - 1):
        cat1 = list(positions.keys())[i]
        cat2 = list(positions.keys())[i + 1]
        x1, y1 = positions[cat1]
        x2, y2 = positions[cat2]
        
        # Add arrow
        fig.add_annotation(
            x=x2, y=y2,
            ax=x1, ay=y1,
            xref="x", yref="y",
            axref="x", ayref="y",
            showarrow=True,
            arrowhead=3,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor="#555"
        )
    
    # Layout settings
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor="white",
        margin=dict(l=40, r=40, b=85, t=40),
        width=750,
        height=400,
        title="Recommended Architecture Flow"
    )
    
    # Display the figure
    st.plotly_chart(fig, use_container_width=True)
