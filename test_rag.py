#!/usr/bin/env python3
"""
Test script for the RAG service functionality.
"""

import os
from dotenv import load_dotenv
from rag_service import RAGService

def test_rag_service():
    """Test the RAG service functionality."""
    print("🧪 Testing RAG Service...")
    
    # Load environment variables
    load_dotenv()
    
    # Check if API key is available
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ GOOGLE_API_KEY not found in environment variables")
        print("Please create a .env file with your Google API key")
        return False
    
    try:
        # Initialize RAG service
        print("📚 Initializing RAG service...")
        rag_service = RAGService()
        
        # Test environment validation
        print("🔍 Validating environment...")
        rag_service.validate_environment()
        print("✅ Environment validation passed")
        
        # Test document loading
        print("🌐 Loading documents...")
        documents = rag_service.load_documents()
        print(f"✅ Loaded {len(documents)} documents")
        
        # Test document splitting
        print("✂️ Splitting documents...")
        docs = rag_service.split_documents()
        print(f"✅ Created {len(docs)} document chunks")
        
        # Test embeddings creation
        print("🧠 Creating embeddings...")
        rag_service.create_embeddings()
        print("✅ Embeddings created successfully")
        
        # Test vector store creation
        print("🗄️ Creating vector store...")
        rag_service.create_vectorstore(docs)
        print("✅ Vector store created successfully")
        
        # Test retriever creation
        print("🔍 Creating retriever...")
        rag_service.create_retriever()
        print("✅ Retriever created successfully")
        
        # Test RAG chain creation
        print("🔗 Creating RAG chain...")
        rag_chain = rag_service.create_rag_chain()
        print("✅ RAG chain created successfully")
        
        # Test query functionality
        print("❓ Testing query functionality...")
        test_question = "What services do you provide?"
        response = rag_service.query(test_question)
        print(f"✅ Query successful!")
        print(f"Question: {test_question}")
        print(f"Answer: {response['answer']}")
        
        # Test document retrieval
        print("📄 Testing document retrieval...")
        relevant_docs = rag_service.get_relevant_documents(test_question)
        print(f"✅ Retrieved {len(relevant_docs)} relevant documents")
        
        print("\n🎉 All tests passed! RAG service is working correctly.")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_rag_service()
    exit(0 if success else 1)
