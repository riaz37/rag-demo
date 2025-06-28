#!/usr/bin/env python3
"""
Health check script to verify the app is ready for deployment.
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if environment is properly set up."""
    print("🔍 Checking environment...")
    
    # Load environment variables
    load_dotenv()
    
    # Check for required environment variable
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ GOOGLE_API_KEY not found in environment")
        return False
    
    print("✅ Environment variables OK")
    return True

def check_imports():
    """Check if all required packages can be imported."""
    print("📦 Checking imports...")
    
    required_packages = [
        'streamlit',
        'langchain',
        'langchain_google_genai',
        'langchain_chroma',
        'langchain_community',
        'dotenv',
        'chromadb'
    ]
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            return False
    
    return True

def check_files():
    """Check if all required files exist."""
    print("📁 Checking required files...")
    
    required_files = [
        'app.py',
        'rag_service.py',
        'config.py',
        'requirements.txt',
        '.env.example',
        'README.md'
    ]
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} not found")
            return False
    
    return True

def check_syntax():
    """Check Python syntax of main files."""
    print("🔍 Checking Python syntax...")
    
    python_files = ['app.py', 'rag_service.py', 'config.py']
    
    for file in python_files:
        try:
            with open(file, 'r') as f:
                compile(f.read(), file, 'exec')
            print(f"✅ {file} syntax OK")
        except SyntaxError as e:
            print(f"❌ {file} syntax error: {e}")
            return False
        except Exception as e:
            print(f"❌ {file} error: {e}")
            return False
    
    return True

def main():
    """Run all health checks."""
    print("🏥 Victoria on Move RAG Assistant - Health Check")
    print("=" * 50)
    
    checks = [
        ("Environment", check_environment),
        ("Imports", check_imports),
        ("Files", check_files),
        ("Syntax", check_syntax)
    ]
    
    all_passed = True
    
    for check_name, check_func in checks:
        print(f"\n{check_name}:")
        if not check_func():
            all_passed = False
    
    print("\n" + "=" * 50)
    
    if all_passed:
        print("🎉 All health checks passed! Ready for deployment.")
        print("\n🚀 To deploy:")
        print("1. Run: ./deploy.sh")
        print("2. Push to GitHub")
        print("3. Deploy on Streamlit Community Cloud")
        return True
    else:
        print("❌ Some health checks failed. Please fix the issues before deploying.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
