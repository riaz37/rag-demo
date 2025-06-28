#!/usr/bin/env python3
"""
Launcher script for the Victoria on Move RAG Assistant.
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

def check_environment():
    """Check if the environment is properly set up."""
    print("🔍 Checking environment setup...")
    
    # Load environment variables
    load_dotenv()
    
    # Check for Google API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ GOOGLE_API_KEY not found!")
        print("Please:")
        print("1. Copy .env.example to .env")
        print("2. Add your Google API key to the .env file")
        print("3. Get your API key from: https://makersuite.google.com/app/apikey")
        return False
    
    print("✅ Environment setup looks good!")
    return True

def run_streamlit_app():
    """Run the Streamlit application."""
    try:
        print("🚀 Starting Victoria on Move RAG Assistant...")
        print("📱 The app will open in your default web browser")
        print("🔗 URL: http://localhost:8501")
        print("⏹️ Press Ctrl+C to stop the application")
        print("-" * 50)
        
        # Run streamlit
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
        
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running Streamlit: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
    
    return True

def main():
    """Main function."""
    print("🚚 Victoria on Move - RAG Assistant")
    print("=" * 40)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Run the app
    if not run_streamlit_app():
        sys.exit(1)

if __name__ == "__main__":
    main()
