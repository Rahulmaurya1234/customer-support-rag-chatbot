# app/services/vector_store.py

from langchain_community.vectorstores import FAISS

from app.services.embeddings import embedding_model


class VectorStore:

    @staticmethod
    def create_index(chunks):

        vector_db = FAISS.from_texts(
            texts=chunks,
            embedding=embedding_model
        )

        return vector_db