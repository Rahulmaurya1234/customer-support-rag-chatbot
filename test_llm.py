from app.core.llm import llm

response = llm.invoke(
    "What is FastAPI?"
)

print(response.content)