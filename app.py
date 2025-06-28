import streamlit as st
import os
from dotenv import load_dotenv
from rag_service import RAGService
from config import (
    PAGE_CONFIG,
    SAMPLE_QUESTIONS,
    ABOUT_CONTENT,
    ERROR_MESSAGES,
    SUCCESS_MESSAGES
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(**PAGE_CONFIG)

@st.cache_resource
def initialize_rag_system():
    """Initialize the RAG system with document loading and vector store setup."""
    try:
        rag_service = RAGService()

        # Load documents
        with st.spinner("Loading documents from Victoria on Move website..."):
            rag_service.load_documents()

        # Split documents
        with st.spinner("Processing documents..."):
            docs = rag_service.split_documents()

        # Create embeddings
        with st.spinner("Creating embeddings..."):
            rag_service.create_embeddings()

        # Create vector store
        with st.spinner("Setting up vector database..."):
            rag_service.create_vectorstore(docs)

        # Create retriever and RAG chain
        with st.spinner("Initializing AI assistant..."):
            rag_service.create_retriever()
            rag_chain = rag_service.create_rag_chain()

        return rag_chain, len(docs), rag_service

    except Exception as e:
        st.error(f"Error initializing RAG system: {str(e)}")
        return None, 0, None

def main():
    # Header
    st.title("🚚 Victoria on Move - AI Assistant")
    st.markdown("Ask me anything about Victoria on Move's moving and removalist services!")

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info(ABOUT_CONTENT)

        st.header("Sample Questions")
        st.markdown("Click any question below to ask it:")

        for i, question in enumerate(SAMPLE_QUESTIONS):
            if st.button(question, key=f"sample_{i}", use_container_width=True):
                # Add the question to chat history and trigger response
                if 'messages' not in st.session_state:
                    st.session_state.messages = []
                st.session_state.messages.append({"role": "user", "content": question})
                st.rerun()

    # Initialize RAG system
    if 'rag_chain' not in st.session_state:
        rag_chain, doc_count, rag_service = initialize_rag_system()
        if rag_chain:
            st.session_state.rag_chain = rag_chain
            st.session_state.doc_count = doc_count
            st.session_state.rag_service = rag_service
            st.success(SUCCESS_MESSAGES["initialization_complete"].format(doc_count=doc_count))
        else:
            st.error(ERROR_MESSAGES["initialization_failed"])
            st.stop()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Ask me anything about Victoria on Move's services..."):
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response if there's a new user message
    if st.session_state.messages and st.session_state.messages[-1]["role"] == "user":
        user_question = st.session_state.messages[-1]["content"]

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.rag_chain.invoke({"input": user_question})
                    answer = response["answer"]
                    st.markdown(answer)

                    # Add assistant response to chat history
                    st.session_state.messages.append({"role": "assistant", "content": answer})

                except Exception as e:
                    error_msg = f"I'm sorry, I encountered an error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": ERROR_MESSAGES["response_error"]})

    # Clear chat button
    if st.session_state.messages:
        _, col2, _ = st.columns([1, 1, 1])
        with col2:
            if st.button("🗑️ Clear Conversation", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

    # Footer
    st.markdown("---")
    st.markdown("*Powered by LangChain, Google Gemini, and Streamlit*",
                help="This app uses RAG (Retrieval-Augmented Generation) to answer questions about Victoria on Move")

if __name__ == "__main__":
    main()
