from app.services.pdf_loader import PDFLoader
from app.services.chunking import TextChunker
from app.services.vector_store import VectorStore

from app.core.llm import llm


class RAGService:

    @staticmethod
    def ask_question(question: str):

        text = PDFLoader.load_pdf(
            "data/pdfs/sample.pdf"
        )

        chunks = TextChunker.create_chunks(text)

        vector_db = VectorStore.create_index(chunks)

        docs = vector_db.similarity_search(
            question,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
        You are a helpful customer support assistant.

        Context:
        {context}

        Question:
        {question}

        Answer using only the context.
        """

        response = llm.invoke(prompt)

        return response.content