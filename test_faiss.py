# test_faiss.py

from app.services.pdf_loader import PDFLoader
from app.services.chunking import TextChunker
from app.services.vector_store import VectorStore


text = PDFLoader.load_pdf("data/pdfs/sample.pdf")

chunks = TextChunker.create_chunks(text)

vector_db = VectorStore.create_index(chunks)

print("FAISS Index Created")
print("Chunks:", len(chunks))