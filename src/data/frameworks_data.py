"""
Data file containing information about various AI frameworks and tools
"""

# Agent Frameworks
AGENT_FRAMEWORKS = [
    {
        "name": "CrewAI",
        "description": "A framework for orchestrating role-playing autonomous AI agents that collaborate to achieve complex goals.",
        "key_features": [
            "Role-based agents with specialized capabilities",
            "Task delegation and coordination between agents",
            "Process management for agent workflows",
            "Human-in-the-loop capabilities"
        ],
        "github": "https://github.com/joaomdmoura/crewAI",
        "docs": "https://docs.crewai.com/",
        "scalability": 7,  # Good scalability with some limitations on very large agent networks
        "performance": 8,  # Excellent execution speed and resource efficiency
        "ease_of_integration": 7,  # Good API design but requires understanding of agent concepts
        "time_to_market": 8,  # Quick to implement due to intuitive role-based architecture
        "cost_effectiveness": 7,  # Reasonable resource usage but may require more powerful LLMs
        "customizability": 9   # Highly customizable with extensive options for agent behaviors
    },
    {
        "name": "LangGraph",
        "description": "A library for building stateful, multi-actor applications with LLMs, focused on creating dynamic, persistent workflow graphs.",
        "key_features": [
            "State management for LLM conversation flows",
            "Multi-actor conversation orchestration",
            "Directed graph-based workflow definition",
            "Seamless integration with LangChain"
        ],
        "github": "https://github.com/langchain-ai/langgraph",
        "docs": "https://python.langchain.com/docs/langgraph",
        "scalability": 8,  # Very good scalability with graph-based architecture
        "performance": 7,  # Good performance but overhead from graph processing
        "ease_of_integration": 6,  # Moderate learning curve due to graph concepts
        "time_to_market": 7,  # Requires more initial design work for complex workflows
        "cost_effectiveness": 8,  # Efficient token usage through directed processing
        "customizability": 8   # Very flexible with strong state management capabilities
    },
    {
        "name": "Haystack",
        "description": "An end-to-end NLP framework that enables you to build powerful search systems and question answering applications.",
        "key_features": [
            "Modular pipeline architecture",
            "Advanced document retrieval capabilities",
            "Pre-trained models for various NLP tasks",
            "Integrations with popular databases and search engines"
        ],
        "github": "https://github.com/deepset-ai/haystack",
        "docs": "https://docs.haystack.deepset.ai/",
        "scalability": 9,  # Excellent scalability with production-ready distributed architecture
        "performance": 8,  # High-performance with optimized retrieval algorithms
        "ease_of_integration": 7,  # Well-documented with good examples but specific conceptual model
        "time_to_market": 7,  # Moderate time to implement due to pipeline complexity
        "cost_effectiveness": 8,  # Good efficiency with caching and optimization features
        "customizability": 7   # Good customization but within the boundaries of the pipeline pattern
    },
    {
        "name": "AutoGen",
        "description": "A framework for building multi-agent systems with conversational LLMs from Microsoft Research.",
        "key_features": [
            "Multi-agent conversation orchestration",
            "Human-AI collaboration capabilities",
            "Customizable agent behaviors",
            "Flexible conversation patterns"
        ],
        "github": "https://github.com/microsoft/autogen",
        "docs": "https://microsoft.github.io/autogen/",
        "scalability": 8,  # Strong scalability with Microsoft's enterprise backing
        "performance": 8,  # Efficient message passing and processing architecture
        "ease_of_integration": 6,  # Steeper learning curve with unique conversation patterns
        "time_to_market": 7,  # Requires understanding of conversation management concepts
        "cost_effectiveness": 8,  # Good token efficiency with proper configuration
        "customizability": 9   # Extremely flexible agent design with extensive configuration options
    },
    {
        "name": "Microsoft Semantic Kernel",
        "description": "A lightweight SDK that integrates LLMs with conventional programming languages through 'Skills' and semantic functions.",
        "key_features": [
            "Plugin architecture for integrating AI capabilities",
            "Memory management for context persistence",
            "Planning for complex task orchestration",
            "Cross-language support (Python, C#)"
        ],
        "github": "https://github.com/microsoft/semantic-kernel",
        "docs": "https://learn.microsoft.com/en-us/semantic-kernel/",
        "scalability": 9,  # Excellent enterprise-grade scalability with Microsoft backing
        "performance": 8,  # Well-optimized with strong architectural design
        "ease_of_integration": 7,  # Good developer experience but requires solid programming skills
        "time_to_market": 6,  # Higher initial investment in skill and plugin development
        "cost_effectiveness": 7,  # Good efficiency but requires proper configuration
        "customizability": 8   # Very adaptable through plugin architecture and memory systems
    }
]

# RAG and Vector Database Solutions
RAG_FRAMEWORKS = [
    {
        "name": "Neo4j",
        "description": "A native graph database platform that helps organizations make sense of their data by revealing how people, processes and systems are interrelated.",
        "key_features": [
            "Graph-based storage for complex relationships",
            "Cypher query language for graph traversal",
            "Vector search capabilities for embedding storage",
            "ACID compliance for data reliability"
        ],
        "github": "https://github.com/neo4j/neo4j",
        "docs": "https://neo4j.com/docs/",
        "scalability": 8,  # Very good scalability with enterprise clustering capabilities
        "performance": 8,  # Excellent query performance for graph relationships
        "ease_of_integration": 7,  # Good APIs but requires learning Cypher query language
        "time_to_market": 6,  # Requires time investment in data modeling and graph design
        "cost_effectiveness": 6,  # Higher resource usage and potential licensing costs
        "customizability": 9   # Extremely flexible graph model for complex relationships
    },
    {
        "name": "pgvector",
        "description": "A PostgreSQL extension for vector similarity search, enabling embedding storage directly in a relational database.",
        "key_features": [
            "Vector similarity search with various distance metrics",
            "Indexing support for faster queries",
            "Integration with existing PostgreSQL data",
            "Open-source and free to use"
        ],
        "github": "https://github.com/pgvector/pgvector",
        "docs": "https://github.com/pgvector/pgvector#readme",
        "scalability": 7,  # Good scalability leveraging PostgreSQL's capabilities
        "performance": 7,  # Good performance but not optimized specifically for vectors
        "ease_of_integration": 8,  # Very easy if already using PostgreSQL
        "time_to_market": 8,  # Quick to implement with familiar SQL patterns
        "cost_effectiveness": 9,  # Very cost-effective as an extension to existing PostgreSQL
        "customizability": 7   # Good flexibility within SQL constraints
    },
    {
        "name": "MongoDB Atlas",
        "description": "A cloud document database with integrated vector search capabilities for building AI-powered applications.",
        "key_features": [
            "Vector search integration with document storage",
            "Managed service with automatic scaling",
            "Atlas Search for text and vector search",
            "Multi-region deployment options"
        ],
        "docs": "https://www.mongodb.com/docs/atlas/",
        "scalability": 9,  # Excellent auto-scaling managed service
        "performance": 8,  # Very good performance with optimized vector indexes
        "ease_of_integration": 8,  # Well-designed APIs and extensive language support
        "time_to_market": 9,  # Very quick deployment with managed services
        "cost_effectiveness": 6,  # Higher cost due to managed cloud service pricing
        "customizability": 7   # Good flexibility but within MongoDB's document model
    },
    {
        "name": "Elasticsearch",
        "description": "A distributed, RESTful search and analytics engine that now supports vector search for AI applications.",
        "key_features": [
            "Combined full-text and vector search capabilities",
            "Distributed architecture for scalability",
            "Rich query DSL for complex queries",
            "Observability features built-in"
        ],
        "github": "https://github.com/elastic/elasticsearch",
        "docs": "https://www.elastic.co/guide/index.html",
        "scalability": 9,  # Excellent distributed architecture with horizontal scaling
        "performance": 8,  # Very good performance with specialized indexing
        "ease_of_integration": 7,  # Good REST API but with specific query DSL to learn
        "time_to_market": 7,  # Moderate setup time for proper configuration
        "cost_effectiveness": 7,  # Reasonable resource usage with proper tuning
        "customizability": 8   # Very flexible with extensive configuration options
    },
    {
        "name": "LangChain RAG",
        "description": "A suite of tools and patterns for implementing Retrieval Augmented Generation in the LangChain ecosystem.",
        "key_features": [
            "Document loading, splitting, and embedding",
            "Multiple retriever implementations",
            "Vector store integrations",
            "Evaluation tools for RAG pipelines"
        ],
        "github": "https://github.com/langchain-ai/langchain",
        "docs": "https://python.langchain.com/docs/use_cases/question_answering/",
        "scalability": 8,  # Very good scalability with modular components
        "performance": 7,  # Good performance but overhead from abstraction layers
        "ease_of_integration": 9,  # Extremely easy with abundant examples and documentation
        "time_to_market": 9,  # Very fast implementation with pre-built components
        "cost_effectiveness": 8,  # Good efficiency with caching and streaming options
        "customizability": 9   # Highly customizable with component-based architecture
    }
]

# Quality Assurance and Observability Frameworks
QA_FRAMEWORKS = [
    {
        "name": "RAGAS",
        "description": "A framework for evaluating Retrieval Augmented Generation (RAG) systems with metrics for retrieval quality, answer relevance, and contextual faithfulness.",
        "key_features": [
            "Evaluation metrics for RAG systems",
            "Comparison of different retrieval methods",
            "Faithfulness and relevance measurement",
            "Integration with popular RAG frameworks"
        ],
        "github": "https://github.com/explodinggradients/ragas",
        "docs": "https://docs.ragas.io/",
        "scalability": 7,  # Good scalability for evaluation workloads
        "performance": 8,  # Efficiently implements evaluation metrics
        "ease_of_integration": 8,  # Simple API for RAG evaluation tasks
        "time_to_market": 8,  # Fast implementation with minimal setup
        "cost_effectiveness": 9,  # Very cost-effective with open source availability
        "customizability": 7   # Good flexibility for standard evaluation scenarios
    },
    {
        "name": "Dynatrace",
        "description": "An AI-powered observability platform that can monitor AI applications and provide detailed insights into their performance.",
        "key_features": [
            "End-to-end monitoring for AI systems",
            "Root cause analysis for performance issues",
            "Real-time alerting and anomaly detection",
            "Integration with CI/CD pipelines"
        ],
        "docs": "https://www.dynatrace.com/support/help/",
        "scalability": 9,  # Enterprise-grade scalability with distributed tracing
        "performance": 9,  # High-performance with minimal overhead monitoring
        "ease_of_integration": 7,  # Good integration options but requires configuration
        "time_to_market": 6,  # Longer setup time for comprehensive monitoring
        "cost_effectiveness": 5,  # Higher cost due to enterprise pricing model
        "customizability": 8   # Very configurable with extensive dashboarding options
    },
    {
        "name": "Guardrails AI",
        "description": "A framework for validating and sanitizing LLM inputs and outputs to ensure reliability, safety, and adherence to guidelines.",
        "key_features": [
            "Input and output validation for LLMs",
            "Customizable validation rules",
            "Structured outputs enforcement",
            "Integration with popular LLM frameworks"
        ],
        "github": "https://github.com/guardrails-ai/guardrails",
        "docs": "https://docs.guardrailsai.com/",
        "scalability": 8,  # Strong scalability with lightweight validation approach
        "performance": 7,  # Good performance with some overhead for validation
        "ease_of_integration": 8,  # Simple API with declarative rules
        "time_to_market": 9,  # Very quick implementation with predefined validators
        "cost_effectiveness": 8,  # Good value with open source core and efficient validation
        "customizability": 9   # Highly adaptable with custom validation rules
    },
    {
        "name": "Traceloop",
        "description": "An open-source observability tool specifically designed for monitoring LLM applications through the OpenLLMetry standard.",
        "key_features": [
            "OpenTelemetry-based LLM monitoring",
            "Prompt and completion tracking",
            "Performance metrics for LLM calls",
            "Integration with existing observability stacks"
        ],
        "github": "https://github.com/traceloop/openllmetry",
        "docs": "https://traceloop.com/docs",
        "scalability": 8,  # Good scalability with OpenTelemetry foundation
        "performance": 7,  # Reasonable overhead for comprehensive tracing
        "ease_of_integration": 8,  # Simple integration with popular LLM frameworks
        "time_to_market": 8,  # Quick implementation with auto-instrumentation
        "cost_effectiveness": 7,  # Good value but requires backend infrastructure
        "customizability": 7   # Good flexibility within OpenTelemetry standards
    },
    {
        "name": "OpenLLMetry",
        "description": "An open-source standard for LLM observability based on OpenTelemetry, providing a consistent way to collect observability data from LLM applications.",
        "key_features": [
            "Standardized LLM telemetry collection",
            "Cross-framework compatibility",
            "Integration with observability platforms",
            "Support for multiple LLM providers"
        ],
        "github": "https://github.com/traceloop/openllmetry",
        "docs": "https://www.openllmetry.ai/",
        "scalability": 9,  # Excellent scalability as an industry standard
        "performance": 8,  # Well-optimized with minimal overhead
        "ease_of_integration": 7,  # Good integration but requires understanding of standards
        "time_to_market": 7,  # Moderate setup time for proper configuration
        "cost_effectiveness": 8,  # Good cost-benefit ratio with open standards
        "customizability": 7   # Good extensibility within the constraints of the standard
    }
]

# Integration and Interoperability Frameworks
INTEGRATION_FRAMEWORKS = [
    {
        "name": "Model Context Protocol (MCP)",
        "description": "A protocol specification for standardizing communication between AI models and the tools they use, enabling consistent tool usage across different models.",
        "key_features": [
            "Standardized tool calling interface",
            "Cross-model tool compatibility",
            "Rich context sharing",
            "Support for streaming and async operations"
        ],
        "docs": "https://modelcontextprotocol.io/",
        "scalability": 8,  # Strong scalability with standardized interfaces
        "performance": 7,  # Good performance with some overhead for protocol compliance
        "ease_of_integration": 8,  # Well-designed API with clear documentation
        "time_to_market": 7,  # Moderate implementation time for full compliance
        "cost_effectiveness": 9,  # Very cost-effective as an open standard
        "customizability": 8   # Very extensible while maintaining compatibility
    },
    {
        "name": "Google AI Agent-to-Agent (A2A)",
        "description": "A protocol for enabling AI agents to communicate with each other in a standardized way, supporting collaborative problem-solving.",
        "key_features": [
            "Standardized agent communication",
            "Support for multi-agent collaborations",
            "Agent discovery mechanisms",
            "Capability advertisement"
        ],
        "docs": "https://ai.google.dev/",
        "scalability": 9,  # Excellent scalability with Google's infrastructure
        "performance": 8,  # Very good performance with optimized protocol
        "ease_of_integration": 7,  # Good API but requires adherence to Google standards
        "time_to_market": 6,  # Longer implementation time for full compliance
        "cost_effectiveness": 7,  # Good value but may have associated service costs
        "customizability": 8   # Very flexible within the constraints of the protocol
    },
    {
        "name": "BeeAI",
        "description": "An open framework for creating interoperable AI agents that can collaborate across different platforms and systems.",
        "key_features": [
            "Cross-platform agent compatibility",
            "Decentralized agent discovery",
            "Capability exchange protocol",
            "Security and permission management"
        ],
        "scalability": 8,  # Very good scalability with decentralized approach
        "performance": 7,  # Good performance with some overhead for interoperability
        "ease_of_integration": 6,  # Moderate complexity due to decentralized nature
        "time_to_market": 6,  # Longer implementation time due to emerging standard
        "cost_effectiveness": 8,  # Good value as an open framework
        "customizability": 9   # Highly customizable with open design philosophy
    },
    {
        "name": "Agent Network Protocol (ANP)",
        "description": "A protocol specification for enabling agents to form networks, share capabilities, and collaborate on complex tasks.",
        "key_features": [
            "Agent registry and discovery",
            "Capability advertisement and negotiation",
            "Task delegation and results sharing",
            "Security and identity verification"
        ],
        "scalability": 8,  # Strong scalability for agent networks of various sizes
        "performance": 7,  # Good message passing performance with some protocol overhead
        "ease_of_integration": 7,  # Reasonably straightforward API with good documentation
        "time_to_market": 7,  # Average implementation time with moderate learning curve
        "cost_effectiveness": 8,  # Good value with open protocol specifications
        "customizability": 8   # Very adaptable with extension mechanisms
    }
]
