from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


class TextChunker:

    @staticmethod
    def create_chunks(text: str):

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )

        chunks = splitter.split_text(text)

        return chunks