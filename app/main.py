from fastapi import FastAPI

from app.schemas.chat import ChatRequest
from app.services.rag_service import RAGService

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):

    answer = RAGService.ask_question(
        request.question
    )

    return {
        "answer": answer
    }