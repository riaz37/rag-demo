"""
RAG Service module for Victoria on Move application.
Handles document loading, embedding, and retrieval functionality.
"""

import os
from typing import List, Tuple, Optional
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import Document

from config import (
    VICTORIA_ON_MOVE_URLS,
    EMBEDDING_MODEL,
    LLM_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    RETRIEVAL_TYPE,
    RETRIEVAL_K,
    SYSTEM_PROMPT
)


class RAGService:
    """
    Service class for handling RAG (Retrieval-Augmented Generation) operations.
    """
    
    def __init__(self):
        """Initialize the RAG service."""
        self.documents: List[Document] = []
        self.vectorstore: Optional[Chroma] = None
        self.retriever = None
        self.rag_chain = None
        self.embeddings = None
        self.llm = None
        
    def validate_environment(self) -> bool:
        """
        Validate that required environment variables are set.
        
        Returns:
            bool: True if environment is valid, False otherwise
        """
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        return True
    
    def load_documents(self, urls: List[str] = None) -> List[Document]:
        """
        Load documents from specified URLs.
        
        Args:
            urls: List of URLs to load. If None, uses default URLs from config.
            
        Returns:
            List of loaded documents
            
        Raises:
            Exception: If document loading fails
        """
        if urls is None:
            urls = VICTORIA_ON_MOVE_URLS
            
        try:
            loader = UnstructuredURLLoader(urls=urls)
            self.documents = loader.load()
            return self.documents
        except Exception as e:
            raise Exception(f"Failed to load documents: {str(e)}")
    
    def split_documents(self, documents: List[Document] = None) -> List[Document]:
        """
        Split documents into smaller chunks.
        
        Args:
            documents: List of documents to split. If None, uses loaded documents.
            
        Returns:
            List of document chunks
        """
        if documents is None:
            documents = self.documents
            
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        return text_splitter.split_documents(documents)
    
    def create_embeddings(self) -> GoogleGenerativeAIEmbeddings:
        """
        Create embeddings model.
        
        Returns:
            GoogleGenerativeAIEmbeddings instance
        """
        self.embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
        return self.embeddings
    
    def create_vectorstore(self, docs: List[Document]) -> Chroma:
        """
        Create vector store from documents.
        
        Args:
            docs: List of document chunks
            
        Returns:
            Chroma vector store instance
        """
        if self.embeddings is None:
            self.create_embeddings()
            
        self.vectorstore = Chroma.from_documents(
            documents=docs, 
            embedding=self.embeddings
        )
        return self.vectorstore
    
    def create_retriever(self):
        """
        Create retriever from vector store.
        
        Returns:
            Retriever instance
        """
        if self.vectorstore is None:
            raise ValueError("Vector store must be created before retriever")
            
        self.retriever = self.vectorstore.as_retriever(
            search_type=RETRIEVAL_TYPE,
            search_kwargs={"k": RETRIEVAL_K}
        )
        return self.retriever
    
    def create_llm(self) -> GoogleGenerativeAI:
        """
        Create LLM instance.
        
        Returns:
            GoogleGenerativeAI instance
        """
        self.llm = GoogleGenerativeAI(model=LLM_MODEL)
        return self.llm
    
    def create_rag_chain(self):
        """
        Create the complete RAG chain.
        
        Returns:
            RAG chain instance
        """
        if self.retriever is None:
            raise ValueError("Retriever must be created before RAG chain")
            
        if self.llm is None:
            self.create_llm()
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", SYSTEM_PROMPT),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(self.llm, prompt)
        self.rag_chain = create_retrieval_chain(self.retriever, question_answer_chain)
        
        return self.rag_chain
    
    def initialize_complete_system(self, urls: List[str] = None) -> Tuple[any, int]:
        """
        Initialize the complete RAG system.
        
        Args:
            urls: List of URLs to load. If None, uses default URLs.
            
        Returns:
            Tuple of (rag_chain, document_count)
            
        Raises:
            Exception: If initialization fails
        """
        try:
            # Validate environment
            self.validate_environment()
            
            # Load and process documents
            documents = self.load_documents(urls)
            docs = self.split_documents(documents)
            
            # Create embeddings and vector store
            self.create_embeddings()
            self.create_vectorstore(docs)
            
            # Create retriever and RAG chain
            self.create_retriever()
            rag_chain = self.create_rag_chain()
            
            return rag_chain, len(docs)
            
        except Exception as e:
            raise Exception(f"Failed to initialize RAG system: {str(e)}")
    
    def query(self, question: str) -> dict:
        """
        Query the RAG system with a question.
        
        Args:
            question: The question to ask
            
        Returns:
            Dictionary containing the response
            
        Raises:
            ValueError: If RAG chain is not initialized
        """
        if self.rag_chain is None:
            raise ValueError("RAG chain must be initialized before querying")
            
        try:
            response = self.rag_chain.invoke({"input": question})
            return response
        except Exception as e:
            raise Exception(f"Error processing query: {str(e)}")
    
    def get_relevant_documents(self, question: str) -> List[Document]:
        """
        Get relevant documents for a question without generating an answer.
        
        Args:
            question: The question to search for
            
        Returns:
            List of relevant documents
        """
        if self.retriever is None:
            raise ValueError("Retriever must be initialized before searching")
            
        return self.retriever.invoke(question)
