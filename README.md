# 🌟 Krushna-Vani: Chat with the Bhagavad Gita 🕉️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-orange.svg)](https://www.pinecone.io/)
[![LangChain](https://img.shields.io/badge/LangChain-AI-yellow.svg)](https://www.langchain.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.5--flash-red.svg)](https://ai.google.dev/)

## 📖 Description

**Krushna-Vani** is a Retrieval-Augmented Generation (RAG) based AI system designed to connect users with the timeless wisdom of the Bhagavad Gita. By leveraging multilingual embedding models and advanced vector search, this project enables interactive conversations with the sacred text, making its profound teachings accessible to everyone, especially the youth of India.

The core mission is to democratize access to the Gita's teachings, which are believed to provide solutions to life's challenges. Through this AI-powered interface, users can ask questions and receive simplified, contextually accurate responses grounded in the scripture, fostering personal growth and spiritual understanding.

## ✨ Features

- **🗣️ Interactive Chat**: Engage in natural conversations with the Bhagavad Gita
- **🌐 Multilingual Support**: Powered by Jina AI's multilingual embedding model for diverse language understanding
- **🔍 Semantic Search**: Advanced vector search using Pinecone for precise context retrieval
- **🤖 AI-Powered Responses**: Utilizes Google Gemini 2.5-flash for intelligent, context-aware answers
- **📚 Faithful to Scripture**: Responses strictly based on retrieved content, no hallucinations
- **🎯 Youth-Friendly**: Simplified explanations tailored for young learners
- **⚡ FastAPI Backend**: High-performance REST API for seamless integration
- **🛡️ Validated Inputs**: Pydantic-based input validation for robust data handling

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Pinecone account and API key
- Google AI API key
- Jina AI API key

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/krushna-vani.git
   cd krushna-vani
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory with the following variables:
   ```env
   GOOGLE_API_KEY=your_google_ai_api_key
   PINECONE_API_KEY=your_pinecone_api_key
   JINA_API_KEY=your_jina_ai_api_key
   ```

5. **Prepare the Data**

   Ensure the Bhagavad Gita PDF is placed in the correct location:
   ```
   Embedding_Pipeline/Data_Processing/Books/Bhagavad-gita_As_It_Is english.pdf
   ```

6. **Ingest Data into Vector Database**
   ```bash
   python ingest_data.py
   ```

## 🚀 Usage

### Running the Application

1. **Start the FastAPI Server**
   ```bash
   uvicorn api:app --reload
   ```

2. **Access the API**

   The API will be available at `http://127.0.0.1:8000`

   - **Home Endpoint**: `GET /`
   - **Health Check**: `GET /health`
   - **Chat Endpoint**: `POST /Chat`

### API Documentation

Visit `http://127.0.0.1:8000/docs` for interactive Swagger UI documentation.

### Example Chat Request

```bash
curl -X POST "http://127.0.0.1:8000/Chat" \
     -H "Content-Type: application/json" \
     -d '{"Input": "How can I overcome fear in difficult situations?"}'
```

### Response Format

```json
{
  "response": "1. Simple Explanation:\n   [Simplified answer based on Gita teachings]\n\n2. Actual Verse from the Context:\n   [Exact verse quotation]\n\n3. Meta Data:\n   - Shlok (Verse) number: [Verse number]\n   - Adhyay (Chapter) number: [Chapter number]\n   - Other citation: [Additional info]"
}
```

## 📁 Project Structure

```
Krushna-Vani/
│
├── api.py                          # Main FastAPI application
├── ingest_data.py                  # Data ingestion script
├── requirements.txt                # Python dependencies
├── temp.py                         # Temporary testing script
│
├── AI_Pipeline/                    # AI response generation pipeline
│   ├── client.py                   # Response generation client
│   ├── model.py                    # Google Gemini model configuration
│   ├── prompt.py                   # Prompt construction logic
│   ├── Prompt_Template.json        # LangChain prompt template
│   └── System_Prompt.py            # AI system prompt
│
├── Embedding_Pipeline/             # Data processing and embedding pipeline
│   ├── Pinecone_setup.py           # Pinecone client setup
│   └── Data_Processing/            # Data cleaning and processing
│       ├── __init__.py
│       ├── chunker.py              # Text chunking logic
│       ├── cleaner.py              # PDF text extraction and cleaning
│       ├── loader.py               # PDF loading functionality
│       └── Books/                  # Source documents
│           └── Bhagavad-gita_As_It_Is english.pdf
│   └── Embedding/                  # Embedding generation
│       └── Embedder.py             # Jina AI embedding client
│   └── vector_db/                  # Vector database operations
│       ├── Index_handler.py        # Pinecone index management
│       └── pinecone_vector.py      # Vector creation and formatting
│
├── Schemas/                        # Pydantic data models
│   └── Chat_validator.py           # Chat input validation
│
├── Vector_Search/                  # Vector similarity search
│   └── Search.py                   # Pinecone query logic
│
└── README.md                       # Project documentation
```

## 🔧 Configuration

### Environment Variables

- `GOOGLE_API_KEY`: Your Google AI API key for Gemini model
- `PINECONE_API_KEY`: Your Pinecone API key for vector database
- `JINA_API_KEY`: Your Jina AI API key for embeddings

### Model Configuration

- **Embedding Model**: Jina CLIP V2 (1024 dimensions)
- **LLM**: Google Gemini 2.5-flash
- **Vector DB**: Pinecone with cosine similarity
- **Chunking Strategy**: Page-based text splitting

## 🤝 Contributing

We welcome contributions to enhance Krushna-Vani! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bhagavad Gita**: The sacred scripture that inspires this project
- **Srila Prabhupada**: For the "As It Is" translation used in the dataset
- **Open Source Community**: For the amazing tools and libraries that made this possible

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or reach out to the maintainers.

---

*May the wisdom of the Bhagavad Gita illuminate your path and guide you towards a life of purpose and peace.* 🕉️
