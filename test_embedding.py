from app.services.embeddings import embedding_model

vector = embedding_model.embed_query(
    "What is refund policy?"
)

print(len(vector))
print(vector[:5])