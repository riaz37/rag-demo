"""
Configuration settings for the Victoria on Move RAG application.
"""

# Website URLs to scrape
VICTORIA_ON_MOVE_URLS = [
    'https://www.victoriaonmove.com.au/local-removalists.html',
    'https://victoriaonmove.com.au/index.html',
    'https://victoriaonmove.com.au/contact.html'
]

# Model configurations
EMBEDDING_MODEL = "models/embedding-001"
LLM_MODEL = "gemini-2.0-flash"

# Text splitting configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval configuration
RETRIEVAL_TYPE = "similarity"
RETRIEVAL_K = 3

# System prompt for the RAG chain
SYSTEM_PROMPT = (
    "You are an assistant for question-answering tasks about Victoria on Move, "
    "a moving and removalist company in Melbourne. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

# Streamlit page configuration
PAGE_CONFIG = {
    "page_title": "Victoria on Move - RAG Assistant",
    "page_icon": "🚚",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Sample questions for the sidebar
SAMPLE_QUESTIONS = [
    "What services do you provide?",
    "What truck sizes are available?",
    "Do you offer interstate moving?",
    "What are your contact details?",
    "Do you provide packing services?",
    "What areas do you cover?",
    "How much does it cost to move a 2-bedroom home?",
    "Do you have insurance coverage?",
    "What equipment do you use for moving furniture?",
    "Can you help with office relocations?"
]

# CSS styling
CUSTOM_CSS = """
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        margin-bottom: 2rem;
        font-size: 2.5rem;
        font-weight: bold;
    }
    .chat-container {
        background-color: rgba(248, 249, 250, 0.1);
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .user-message {
        background-color: rgba(33, 150, 243, 0.1);
        color: var(--text-color, #000000);
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #2196F3;
        border: 1px solid rgba(33, 150, 243, 0.3);
    }
    .assistant-message {
        background-color: rgba(76, 175, 80, 0.1);
        color: var(--text-color, #000000);
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CAF50;
        border: 1px solid rgba(76, 175, 80, 0.3);
    }
    .sidebar-info {
        background-color: rgba(240, 242, 246, 0.1);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid rgba(240, 242, 246, 0.3);
    }
    .sample-question-btn {
        width: 100%;
        margin: 0.2rem 0;
        text-align: left;
    }
    .footer {
        text-align: center;
        color: #666;
        font-style: italic;
        margin-top: 2rem;
    }

    /* Dark theme support */
    @media (prefers-color-scheme: dark) {
        .user-message {
            background-color: rgba(33, 150, 243, 0.2);
            color: #ffffff;
            border: 1px solid rgba(33, 150, 243, 0.5);
        }
        .assistant-message {
            background-color: rgba(76, 175, 80, 0.2);
            color: #ffffff;
            border: 1px solid rgba(76, 175, 80, 0.5);
        }
        .sidebar-info {
            background-color: rgba(240, 242, 246, 0.1);
            color: #ffffff;
            border: 1px solid rgba(240, 242, 246, 0.3);
        }
        .footer {
            color: #cccccc;
        }
    }

    /* Force text visibility in Streamlit dark theme */
    .user-message strong,
    .assistant-message strong {
        color: inherit !important;
    }

    /* Ensure text is visible in both themes */
    [data-testid="stMarkdownContainer"] .user-message,
    [data-testid="stMarkdownContainer"] .assistant-message {
        color: var(--text-color) !important;
    }

    /* Streamlit dark theme overrides */
    .stApp[data-theme="dark"] .user-message {
        background-color: rgba(33, 150, 243, 0.15) !important;
        color: #ffffff !important;
        border: 1px solid rgba(33, 150, 243, 0.4) !important;
    }

    .stApp[data-theme="dark"] .assistant-message {
        background-color: rgba(76, 175, 80, 0.15) !important;
        color: #ffffff !important;
        border: 1px solid rgba(76, 175, 80, 0.4) !important;
    }

    .stApp[data-theme="dark"] .sidebar-info {
        background-color: rgba(240, 242, 246, 0.05) !important;
        color: #ffffff !important;
        border: 1px solid rgba(240, 242, 246, 0.2) !important;
    }
</style>
"""

# About section content
ABOUT_CONTENT = """
This AI assistant can answer questions about Victoria on Move's 
moving and removalist services in Melbourne.

**Features:**
- Local and interstate moving services
- Furniture removal and packing
- Different truck sizes available
- Professional moving team
- Insurance coverage
- Customized moving plans

**How it works:**
1. Ask any question about Victoria on Move
2. The AI searches through company information
3. Get accurate, contextual answers instantly
"""

# Error messages
ERROR_MESSAGES = {
    "initialization_failed": "❌ Failed to initialize RAG system. Please check your API keys and try again.",
    "response_error": "I'm sorry, I encountered an error while processing your question.",
    "no_api_key": "Please set your GOOGLE_API_KEY in the env",
    "loading_failed": "Failed to load documents from the website. Please check your internet connection."
}

# Success messages
SUCCESS_MESSAGES = {
    "initialization_complete": "✅ RAG system initialized successfully! Processed {doc_count} document chunks.",
    "ready_to_chat": "🤖 Ready to answer your questions about Victoria on Move!"
}
