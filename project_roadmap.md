Phase 0 → Theory ✅ Completed

Phase 1 → Project Setup
    - Virtual Environment
    - Dependencies
    - Folder Structure
    - Environment Variables
    - API Key Configuration

Phase 2 → FastAPI Setup

Phase 3 → PDF Loading

Phase 4 → Chunking

Phase 5 → Embeddings

Phase 6 → FAISS Indexing

Phase 7 → Retrieval

Phase 8 → Gemini/OpenAI Integration

Phase 9 → Complete RAG Pipeline

Phase 10 → FAQ Integration

Phase 11 → Production Ready APIs


phase 1:
step1:mkdir customer_chatbot
cd customer_chatbot
verify:
pwd : Users/main/Desktop/customer_chatbot
step 2:crete vertual enviroment
python3 -m venv .venv
step 3: Activate the vertual enviroment
source .venv/bin/activate
veify python
which python
# why need dependency because run server for api running

# FastAPI

POST /chat

POST /upload

GET /health

# Run fats api = 
```
uvicorn app.main:app --reload
```
# longchain
Purpose:orchestration layer 
Handles:
    Loaders
    Splitters
    Embeddings
    Retrieval

# Llamaindex
purpose:knownladge
specifized of 
Documentation
retrival
indexing

# Faiss
vectore serachin

# pypdf
pdf -> text

# python-dotenv
Read .env variables

# pydantic
Request Validation

# googel genarative ai
# purpose
        Gemini LLM
        Gemini Embeddings

# open ai
# pupose
    GPT Models
    Embedding Models

# step 4 dependency install 

if using google api 

pip install fastapi uvicorn langchain langchain-community llama-index faiss-cpu pypdf python-dotenv pydantic google-genai

if using open ai 

pip install fastapi uvicorn langchain langchain-community llama-index faiss-cpu pypdf python-dotenv pydantic openai

# save dependency

pip freeze > requirements.txt

requirements.txt

1. FastAPI
2. PDF Loading
3. Chunking
4. Embeddings
5. FAISS
6. Retrieval
7. LangChain RAG
8. LlamaIndex RAG
9. Hybrid RAG


Browser
   ↓
HTTP Request
   ↓
Uvicorn Server
   ↓
FastAPI Application
   ↓
Route Matching
   ↓
@app.get("/health")
   ↓
Function Execute
   ↓
JSON Response
   ↓
Uvicorn
   ↓
Browser

ASGI = Asynchronous Server Gateway Interface

Uvicorn
↔
FastAPI

Browser
 ↓
Uvicorn (ASGI Server)
 ↓
FastAPI (ASGI App)
 ↓
Response

uvicorn app.main:app --reload