# Victoria on Move - RAG Assistant 🚚

A Retrieval-Augmented Generation (RAG) application that provides intelligent answers about Victoria on Move's moving and removalist services in Melbourne. Built with LangChain, Google Gemini, and Streamlit.

## Features

- **Intelligent Q&A**: Ask questions about Victoria on Move's services and get accurate, contextual answers
- **Real-time Information**: Loads and processes content from the company's website
- **Interactive Chat Interface**: User-friendly Streamlit web interface with chat history
- **Sample Questions**: Pre-built questions to help users get started
- **Modular Architecture**: Clean, maintainable code structure
- **Optimized Vector Search**: FAISS-powered similarity search for fast and accurate retrieval
- **Cloud-Ready**: Optimized for deployment on Streamlit Community Cloud

## Services Covered

The AI assistant can answer questions about:
- Local and interstate moving services
- Furniture removal and packing
- Different truck sizes and pricing
- Professional moving team services
- Insurance coverage
- Customized moving plans
- Contact information and service areas

## Technology Stack

- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.0 Flash
- **Embeddings**: Google Generative AI Embeddings
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Framework**: LangChain
- **Language**: Python 3.8+

## Installation

### Prerequisites

- Python 3.8 or higher
- Google API Key (for Gemini and Embeddings)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rag_demo
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your Google API key:
   ```
   GOOGLE_API_KEY=your_actual_google_api_key_here
   ```

5. **Get Google API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Copy the key to your `.env` file

## Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using the Interface

1. **Ask Questions**: Type your question in the input field or click on sample questions in the sidebar
2. **View Responses**: The AI will provide contextual answers based on Victoria on Move's website content
3. **Chat History**: Previous questions and answers are displayed in the conversation area
4. **Clear Chat**: Use the "Clear Conversation" button to start fresh

### Sample Questions

- "What services do you provide?"
- "What truck sizes are available?"
- "Do you offer interstate moving?"
- "What are your contact details?"
- "Do you provide packing services?"
- "What areas do you cover?"

## Project Structure

```
rag_demo/
├── app.py                    # Main Streamlit application
├── rag_service.py            # RAG functionality service class
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── packages.txt              # System packages for deployment
├── .env.example             # Environment variables template
├── .env                     # Environment variables (create from .env.example)
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── deploy_guide.md          # Deployment instructions
├── health_check.py          # Pre-deployment validation
├── deploy.sh                # Deployment automation script
├── README.md                # Project documentation
└── venv/                    # Virtual environment
```

## Configuration

The application can be configured through `config.py`:

- **URLs**: Website URLs to scrape for content
- **Models**: LLM and embedding model names
- **Chunk Settings**: Text splitting parameters
- **Retrieval Settings**: Vector search parameters
- **UI Settings**: Streamlit page configuration and styling

## Development

### Adding New URLs

To include additional website pages:

1. Edit `config.py`
2. Add URLs to the `VICTORIA_ON_MOVE_URLS` list
3. Restart the application

### Customizing the System Prompt

Modify the `SYSTEM_PROMPT` in `config.py` to change how the AI responds to questions.

### Styling

The application uses Streamlit's native components for optimal theme compatibility. The interface automatically adapts to light and dark themes.

## Deployment

### Streamlit Community Cloud (Recommended)

The application is optimized for deployment on Streamlit Community Cloud:

1. **Push to GitHub**: Ensure your code is in a GitHub repository
2. **Deploy on Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Select the main branch and `app.py` as the main file
3. **Configure Secrets**: Add your `GOOGLE_API_KEY` in the app's secrets management
4. **Deploy**: The app will automatically deploy with all dependencies

### Local Development

For local development and testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Run health check
python health_check.py

# Start the application
streamlit run app.py
```

### Other Platforms

The application can also be deployed on:
- **Heroku**: Use the provided configuration files
- **Railway**: Direct deployment from GitHub
- **Render**: Web service deployment
- **Google Cloud Run**: Containerized deployment

See `deploy_guide.md` for detailed platform-specific instructions.

## Troubleshooting

### Common Issues

1. **API Key Error**: Ensure your Google API key is correctly set in the `.env` file
2. **Import Errors**: Make sure all dependencies are installed with `pip install -r requirements.txt`
3. **Loading Issues**: Check your internet connection for website content loading
4. **Memory Issues**: The app uses FAISS for efficient memory usage, but restart if needed
5. **Deployment Issues**: Run `python health_check.py` before deploying to catch common problems

### Error Messages

The application provides helpful error messages for common issues:
- Missing API key
- Failed document loading
- Initialization errors
- Query processing errors

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for demonstration purposes. Please respect Victoria on Move's website terms of service when using their content.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the error messages in the application
3. Ensure all dependencies are correctly installed
4. Verify your Google API key is valid and has the necessary permissions
