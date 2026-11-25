from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .config import MODEL_NAME
from .chat_model import chat_model
from .memory import (
    get_history,
    add_message,
    clear_history
)
from .rag import (
    retrieve_documents,
    build_rag_prompt
)


app = FastAPI(
    title="AI Chatbot API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SYSTEM_PROMPT = """
You are AI Chat, an intelligent and helpful AI assistant.

Your goals:
- Give accurate and useful answers.
- Explain difficult concepts clearly.
- Use simple language when appropriate.
- Provide examples when helpful.
- Be honest when uncertain.
- Do not invent facts.
"""


class ChatRequest(BaseModel):

    message: str


@app.get("/")
def home():

    return {
        "message": "AI Chatbot API is running",
        "model": MODEL_NAME
    }


@app.post("/chat")
def chat(request: ChatRequest):

    results = retrieve_documents(
        request.message,
        k=3
    )

    prompt = build_rag_prompt(
        request.message,
        results
    )

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(
        get_history()
    )

    messages.append({
        "role": "user",
        "content": prompt
    })

    answer = chat_model(
        messages
    )

    add_message(
        "user",
        request.message
    )

    add_message(
        "assistant",
        answer
    )

    return {
        "answer": answer,
        "sources": [
            result["source"]
            for result in results
        ]
    }
@app.get("/health")
def health():

    return {
        "status": "healthy",
        "service": "AI Chatbot API",
        "model": MODEL_NAME
    }
@app.delete("/clear-chat")
def clear_chat():

    clear_history()

    return {
        "message": "Chat history cleared successfully"
    }