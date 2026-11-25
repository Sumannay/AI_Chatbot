# AI Chatbot with RAG

An AI-powered full-stack chatbot built with **Python, FastAPI, React, TypeScript, SQLite, and Retrieval-Augmented Generation (RAG)**.

The application allows users to interact with an AI assistant, maintain conversation history, upload documents, and ask questions based on their uploaded files.

## Project Overview

This project aims to build a ChatGPT-style application with document-based question answering.

Unlike a basic chatbot that only processes user prompts, this application also supports document retrieval. It extracts content from uploaded files, searches for relevant information, and provides that information to the language model as context when generating answers.

## Key Features

- **AI-powered conversations:** Interact with a configured LLM provider.
- **Streaming responses:** Receive AI answers progressively using Server-Sent Events (SSE).
- **Conversation management:** Create and manage conversations and access previous chat history.
- **Persistent storage:** Store application data using SQLite and SQLAlchemy.
- **Document uploads:** Upload TXT, PDF, and DOCX documents.
- **Document extraction:** Extract text from PDF and Word documents.
- **RAG-based question answering:** Retrieve relevant document content before generating answers.
- **Hybrid retrieval:** Combine embedding-based retrieval with keyword overlap.
- **Context management:** Use recent conversation messages to maintain conversational context.
- **Voice input:** Use browser-supported speech recognition.
- **Read-aloud:** Listen to chatbot responses using browser speech synthesis.
- **Authentication:** Support email/password authentication and Google/GitHub OAuth when credentials are configured.
- **LLM provider abstraction:** Support configurable OpenAI-compatible LLM providers.
- **Local embedding fallback:** Use deterministic local embeddings when an external embedding provider is unavailable.

## Technology Stack

### Frontend
- React
- TypeScript
- Vite
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite

### AI and RAG
- Large Language Model (LLM) APIs
- Text embeddings
- Hybrid document retrieval
- Keyword matching
- Retrieval-Augmented Generation (RAG)

### Document Processing
- PyMuPDF
- python-docx
- TXT file processing

### Communication
- REST APIs
- Server-Sent Events (SSE)

## System Architecture

The application follows a frontend-backend architecture.

1. The React frontend accepts user messages and document uploads.
2. The frontend sends requests to the FastAPI backend.
3. The backend processes requests and manages application logic.
4. SQLAlchemy interacts with SQLite to persist application data.
5. For document questions, the RAG system retrieves relevant document content.
6. The backend sends the prompt and relevant context to the configured LLM provider.
7. The generated response is streamed back to the frontend using SSE.
8. The frontend displays the response to the user.

## How RAG Works

The application uses Retrieval-Augmented Generation to answer questions using uploaded documents.

### Document Processing

1. The user uploads a TXT, PDF, or DOCX file.
2. The backend identifies the file type.
3. The appropriate document extraction library extracts its text.
4. The extracted content is prepared for retrieval.

### Retrieval Process

1. The user asks a question about an uploaded document.
2. The system searches available document content.
3. Embedding-based retrieval identifies semantically relevant content.
4. Keyword overlap helps identify matching terms.
5. Relevant text is selected and supplied as context to the LLM.

### Answer Generation

1. The backend combines the user's question with retrieved context.
2. The configured LLM generates a response.
3. The response is streamed to the frontend.
4. The user receives an answer informed by the retrieved document content.

**Important:** RAG retrieves information and supplies it to the LLM. It does not mean that the underlying language model has been fine-tuned or retrained.

## Project Structure

The repository includes backend, data, and notebooks directories. The frontend directory should also be included if you are publishing the complete React application.

```text
AI_Chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   └── ...
│   ├── requirements.txt
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── data/
│   └── documents/
│
├── notebooks/
│
├── .env.example
├── .gitignore
└── README.md
```

The tree above describes the intended application layout. Actual filenames and folders may differ depending on your implementation.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sumannay/AI_Chatbot.git
cd AI_Chatbot
```

### 2. Set Up the Python Backend

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the backend dependencies:

```bash
pip install -r backend/requirements.txt
```

If your requirements file is located somewhere else, run the installation command from its actual location.

### 3. Configure Environment Variables

Create a `.env` file using your project's `.env.example` as a reference.

Configure the required values for:

- LLM provider and API credentials
- Database settings, if configurable
- Authentication settings
- Google OAuth credentials, if Google login is enabled
- GitHub OAuth credentials, if GitHub login is enabled

Never upload your actual `.env` file or API keys to GitHub.

### 4. Start the Backend

From the backend directory, activate the appropriate virtual environment and run:

```bash
uvicorn app.main:app --reload
```

The backend should start on the configured local address. The default FastAPI development address is generally:

```text
http://127.0.0.1:8000
```

### 5. Set Up the Frontend

Open a separate terminal and navigate to the React frontend directory.

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Use the local URL displayed by Vite in your terminal.

Make sure the frontend API configuration points to the running backend.

## Document-Based Question Answering

The application supports TXT, PDF, and DOCX documents.

Supported document operations include:

- Upload documents.
- List uploaded documents.
- Delete documents.
- Extract document text.
- Retrieve relevant content for user questions.

The document retrieval system combines embeddings and keyword matching to find useful context.

## Voice Features

The application uses browser-supported speech capabilities.

- Speech recognition allows users to enter messages through their voice.
- Speech synthesis allows users to listen to generated chatbot responses.

Availability depends on browser support and microphone permissions.

## Database

SQLite is used for persistent storage, with SQLAlchemy providing the database abstraction.

The database supports application information such as users, conversations, and messages according to the implemented models.

## LLM Provider Configuration

The application uses a provider abstraction for OpenAI-compatible language model APIs.

The application requires valid provider configuration to generate real LLM responses.

If an LLM provider is not configured, the application should report the configuration issue rather than presenting fabricated AI responses.

## Testing

Run the tests using the test setup and commands provided in the backend project.

Tests should cover important application areas, including:

- API endpoints
- Conversation handling
- Document processing
- Retrieval logic
- Authentication
- LLM provider integration

## Security Considerations

- Keep API keys in environment variables.
- Never commit secrets or credentials.
- Configure OAuth credentials on the server side.
- Validate uploaded files.
- Apply appropriate authentication and authorization checks.
- Use production-grade settings before public deployment.

## Current Limitations and Future Improvements

Potential improvements include:

- Alembic database migrations.
- OCR support for scanned PDFs and images.
- More advanced multi-document citations.
- Usage and API cost tracking.
- Additional automated tests.
- Deployment scripts and production configuration.
- Improved retrieval and ranking strategies.

## Learning Outcomes

Through this project, I gained practical experience in:

- Python backend development.
- Building APIs using FastAPI.
- React and TypeScript frontend development.
- Database integration using SQLite and SQLAlchemy.
- Working with LLM APIs.
- Understanding embeddings and semantic search.
- Implementing RAG-based document question answering.
- Processing PDF, DOCX, and TXT documents.
- Implementing response streaming with SSE.
- Integrating browser-based voice features.
- Managing a full-stack application.

## Author

**Suman Nayak**

GitHub: https://github.com/Sumannay

Project Repository: https://github.com/Sumannay/AI_Chatbot

---

*An AI-powered chatbot project combining full-stack development, language models, and Retrieval-Augmented Generation.*
