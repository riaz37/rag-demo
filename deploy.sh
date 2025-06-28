#!/bin/bash

# Deployment script for Victoria on Move RAG Assistant

echo "🚀 Preparing for deployment..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "📦 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Deploy Victoria on Move RAG Assistant - $(date)"

echo "✅ Ready for deployment!"
echo ""
echo "🌐 Next steps for Streamlit Community Cloud deployment:"
echo "1. Push to GitHub: git remote add origin https://github.com/riaz37/rag-demo"
echo "2. Push code: git push -u origin main"
echo "3. Visit: https://share.streamlit.io/"
echo "4. Connect your GitHub repo and deploy!"
echo "5. Add your GOOGLE_API_KEY in the app secrets"
echo ""
echo "📖 See deploy_guide.md for detailed instructions"
