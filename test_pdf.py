from app.services.pdf_loader import PDFLoader

text = PDFLoader.load_pdf(
    "data/pdfs/sample.pdf"
)

print(text[:1000])