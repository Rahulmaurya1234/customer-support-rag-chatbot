
# PDF & FAQ RAG Chatbot

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Python, FastAPI, LangChain, FAISS, HuggingFace Embeddings, and Gemini.

The chatbot can answer questions from PDF documents by retrieving relevant information from the document and providing context-aware responses using a Large Language Model (LLM).

---

## Features

* PDF document ingestion
* Text extraction using PyPDF
* Intelligent text chunking
* Semantic embeddings generation
* FAISS vector database for similarity search
* Retrieval-Augmented Generation (RAG)
* Gemini LLM integration
* FastAPI REST API
* Swagger documentation

---

## Tech Stack

### Backend

* Python 3.11
* FastAPI
* Uvicorn

### RAG Components

* LangChain
* FAISS
* HuggingFace Embeddings
* Google Gemini

### Document Processing

* PyPDF

---

## Project Architecture

### Indexing Pipeline

PDF Document

↓

Text Extraction (PyPDF)

↓

Chunking

↓

Embeddings Generation

↓

FAISS Vector Store

---

### Query Pipeline

User Question

↓

Question Embedding

↓

FAISS Similarity Search

↓

Top Relevant Chunks

↓

Prompt Construction

↓

Gemini LLM

↓

Final Answer

---

## Folder Structure

```text
customer_chatbot/

├── app/
│
├── core/
│   ├── config.py
│   └── llm.py
│
├── services/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag_service.py
│
├── schemas/
│   └── chat.py
│
├── main.py
│
├── data/
│   └── pdfs/
│       └── sample.pdf
│
├── test_pdf.py
├── test_chunking.py
├── test_embedding.py
├── test_faiss.py
├── test_rag.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository_url>

cd customer_chatbot
```

### Create Environment

```bash
conda create -n py311 python=3.11

conda activate py311
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_api_key

MODEL_NAME=gemini-2.5-flash

CHUNK_SIZE=1000

CHUNK_OVERLAP=200

PDF_FOLDER=data/pdfs

FAISS_INDEX_PATH=data/faiss_index
```

---

## Running the Application

### Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

### Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "question": "What is this PDF about?"
}
```

Response:

```json
{
  "answer": "This PDF is a sample demonstrating the use of bookmarks..."
}
```

---

## RAG Workflow

### Step 1: PDF Loading

The PDF document is loaded using PyPDF.

### Step 2: Chunking

Large text is divided into smaller chunks with overlap.

### Step 3: Embedding Generation

Each chunk is converted into a dense vector representation using HuggingFace Embeddings.

### Step 4: Vector Storage

Vectors are stored inside a FAISS index.

### Step 5: Retrieval

User questions are converted into vectors and searched against FAISS.

### Step 6: Generation

Relevant chunks are provided as context to Gemini for answer generation.

---

## Why RAG?

Traditional LLMs rely only on their training data.

RAG improves accuracy by:

* Retrieving relevant knowledge
* Reducing hallucinations
* Using private company documents
* Providing context-aware answers

---

## Future Improvements

* Persistent FAISS storage
* Multiple PDF support
* FAQ ingestion
* Conversation memory
* Hybrid Search
* Metadata filtering
* Streaming responses
* Production deployment

---

## Author

Rahul Maurya

B.Tech (Artificial Intelligence & Machine Learning)

Kanpur Institute of Technology





conda activate py311

conda deactivate

