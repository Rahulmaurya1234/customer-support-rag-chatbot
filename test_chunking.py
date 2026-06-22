from app.services.pdf_loader import PDFLoader
from app.services.chunking import TextChunker


text = PDFLoader.load_pdf(
    "data/pdfs/sample.pdf"
)

chunks = TextChunker.create_chunks(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0])