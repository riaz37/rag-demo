# 🚀 Deployment Guide for Victoria on Move RAG Assistant

## Option 1: Streamlit Community Cloud (Recommended - FREE)

### Prerequisites
- GitHub account
- Your code pushed to a GitHub repository

### Steps:

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Victoria on Move RAG Assistant"
   git branch -M main
   git remote add origin https://github.com/yourusername/victoria-on-move-rag.git
   git push -u origin main
   ```

2. **Visit Streamlit Community Cloud:**
   - Go to https://share.streamlit.io/
   - Sign in with your GitHub account

3. **Deploy your app:**
   - Click "New app"
   - Select your repository
   - Choose the main branch
   - Set main file path: `app.py`
   - Click "Deploy!"

4. **Set up secrets (Environment Variables):**
   - In your app dashboard, click "Settings" → "Secrets"
   - Add your environment variables:
   ```toml
   GOOGLE_API_KEY = "your_google_api_key_here"
   ```

### Advantages:
- ✅ Completely free
- ✅ Easy to use
- ✅ Automatic deployments from GitHub
- ✅ Built-in secrets management
- ✅ Custom domain support

---

## Option 2: Heroku (Free tier discontinued, paid plans available)

### Prerequisites
- Heroku account
- Heroku CLI installed

### Additional files needed:

1. **Create Procfile:**
   ```
   web: sh setup.sh && streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Create setup.sh:**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [general]\n\
   email = \"your-email@domain.com\"\n\
   " > ~/.streamlit/credentials.toml
   echo "\
   [server]\n\
   headless = true\n\
   enableCORS=false\n\
   port = $PORT\n\
   " > ~/.streamlit/config.toml
   ```

3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   heroku config:set GOOGLE_API_KEY="your_google_api_key_here"
   ```

---

## Option 3: Railway (Modern alternative)

### Steps:
1. Visit https://railway.app/
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard
4. Deploy automatically

---

## Option 4: Render (Free tier available)

### Steps:
1. Visit https://render.com/
2. Connect your GitHub repository
3. Choose "Web Service"
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Add environment variables

---

## Option 5: Local Network Deployment

### For local network access:
```bash
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

Then access via: `http://your-local-ip:8501`

---

## 🔧 Pre-deployment Checklist

- [ ] Code is working locally
- [ ] All dependencies are in requirements.txt
- [ ] Environment variables are properly configured
- [ ] No hardcoded API keys in the code
- [ ] README.md is complete and helpful

---

## 🚨 Important Security Notes

1. **Never commit API keys to GitHub**
2. **Use environment variables for all secrets**
3. **Add .env to .gitignore**
4. **Use secrets management in your deployment platform**

---

## 📝 Recommended: Streamlit Community Cloud

For your Victoria on Move RAG Assistant, I recommend **Streamlit Community Cloud** because:

1. **Free and reliable**
2. **Perfect for Streamlit apps**
3. **Easy GitHub integration**
4. **Built-in secrets management**
5. **Automatic deployments**

Would you like me to help you set up the deployment to Streamlit Community Cloud?
