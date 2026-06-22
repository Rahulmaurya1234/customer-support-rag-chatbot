from app.services.rag_service import RAGService

answer = RAGService.ask_question(
    "What is this PDF about?"
)

print(answer)
