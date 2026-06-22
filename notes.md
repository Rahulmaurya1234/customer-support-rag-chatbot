# RAG Chatbot Learning Notes

# Goal

Build a PDF + FAQ RAG Chatbot using:

* Python
* FastAPI
* LangChain
* LlamaIndex
* FAISS
* OpenAI/Gemini

---

# What is RAG?

RAG = Retrieval Augmented Generation

Instead of relying only on the LLM's training data, we retrieve relevant information from our own documents and provide it to the LLM.

Flow:

User Question
↓
Retrieve Relevant Information
↓
Add Information to Prompt
↓
Generate Answer

---

# Why RAG?

Problem:

LLMs do not know company-specific data such as:

* FAQ documents
* SOPs
* Internal policies
* Customer support manuals
* PDF files

Solution:

Store company knowledge separately and retrieve it when needed.

---

# Complete RAG Architecture

PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store

---

User Question
↓
Question Embedding
↓
FAISS Search
↓
Relevant Chunks
↓
Prompt Construction
↓
LLM
↓
Answer

---

# Two Pipelines

## 1. Indexing Pipeline

Runs once.

PDF
↓
Extract Text
↓
Create Chunks
↓
Generate Embeddings
↓
Store in FAISS

Goal:

Prepare the knowledge base.

---

## 2. Query Pipeline

Runs for every user question.

Question
↓
Question Embedding
↓
FAISS Search
↓
Retrieve Chunks
↓
Prompt
↓
LLM
↓
Answer

Goal:

Answer the user's question.

---

# Chunking

Definition:

Splitting large documents into smaller pieces.

Example:

100-page PDF
↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4

Why chunking?

1. Context limits
2. Faster retrieval
3. Lower cost
4. Better search accuracy

---

# What is an Embedding?

Embedding = Numerical representation of text.

Example:

"refund"
↓
[0.12, 0.55, 0.91]

Purpose:

Convert language into vectors so similarity can be measured.

---

# Why Embeddings are Needed

Keyword matching is weak.

Example:

PDF:

Refund Policy

User:

How do I get my money back?

Keyword search:

refund ≠ money back

Embedding search:

refund ≈ money back

This is semantic search.

---

# Transformer and Embeddings

Transformer creates embeddings.

Flow:

Text
↓
Tokenizer
↓
Token IDs
↓
Embedding Layer
↓
Transformer Layers

Important:

Transformer generates embeddings.

FAISS does not create embeddings.

---

# Words vs Tokens

Word:

Human language unit.

Token:

Unit processed by a model.

Example:

unbelievable

Words = 1

Tokens may be:

un
believ
able

Tokens = 3

---

# Tokenization

Converts text into tokens.

Example:

refund policy

↓

["refund", "policy"]

↓

[1423, 6731]

These numbers are token IDs.

---

# Embedding Layer

Converts token IDs into vectors.

Example:

1423

↓

[0.25, 0.78, 0.31]

Think of it as a giant lookup table.

---

# Vector Space

Embeddings exist in vector space.

Similar meanings are close together.

Example:

refund
money back
reimbursement

Vectors become close.

Example:

refund -> [1.0, 2.0]

money back -> [1.1, 2.1]

reimbursement -> [0.9, 1.9]

---

# Similarity Search

Goal:

Find vectors with similar meaning.

Methods:

1. Cosine Similarity
2. Euclidean Distance

---

# Cosine Similarity

Measures direction.

Question:

Do these vectors point in the same direction?

Range:

-1 to 1

1 = identical direction

0 = unrelated

-1 = opposite direction

Used heavily in RAG systems.

---

# Euclidean Distance

Measures physical distance between vectors.

Question:

How far apart are the points?

Small distance = similar

Large distance = different

---

# What is FAISS?

FAISS = Facebook AI Similarity Search

Created by Meta.

Purpose:

Store vectors and perform fast similarity search.

Example:

Question Vector
↓
FAISS
↓
Top Similar Vectors

---

# What Does FAISS Store?

Primarily vectors.

In RAG systems:

Vector
+
Associated Text
+
Metadata

Example:

Vector:
[0.21, 0.45, 0.78]

Text:
"Refunds are processed within 7 days"

---

# Attention

Core idea of Transformers.

Definition:

Each token decides which other tokens are important for understanding its meaning.

Example:

I deposited money in the bank

When processing:

bank

Attention focuses more on:

money
deposited

Than:

the
in

---

# Self Attention

Tokens attend to other tokens in the same sequence.

Every token asks:

Which tokens should I pay attention to?

---

# Query, Key, Value (QKV)

Every token creates:

Query (Q)
Key (K)
Value (V)

Query:

What information am I looking for?

Key:

What information do I contain?

Value:

Actual information.

Attention compares:

Query with Keys

Then combines Values.

---

# Multi Head Attention

Multiple attention mechanisms run in parallel.

Each head learns different relationships.

Example:

Head 1:
Python ↔ Programming

Head 2:
Rahul ↔ Loves

Head 3:
Programming ↔ Skill

Results are combined.

---

# LangChain

Framework for building LLM applications.

Provides:

* Loaders
* Splitters
* Embeddings
* Retrievers
* Chains
* Agents

Purpose:

Orchestrate the RAG pipeline.

---

# LlamaIndex

Framework focused on:

* Documents
* Indexing
* Retrieval
* Knowledge Bases

Purpose:

Connect external data to LLMs.

Think:

LangChain = Application Framework

LlamaIndex = Knowledge Framework

---

# FastAPI

Backend framework.

Used for:

POST /chat

POST /upload

GET /health

Purpose:

Expose RAG as an API.

---

# Full Production Flow

PDF
↓
Loader
↓
Chunking
↓
Embedding Model
↓
FAISS

User Question
↓
Embedding Model
↓
FAISS Retrieval
↓
Top Chunks
↓
Prompt
↓
Transformer
↓
Answer

---

# Interview Questions

1. What is RAG?
2. Why chunking is needed?
3. What is an embedding?
4. Why are embeddings useful?
5. Difference between keyword search and semantic search?
6. What does FAISS do?
7. What is cosine similarity?
8. What is attention?
9. What is self-attention?
10. What are Query, Key, and Value?
11. Difference between LangChain and LlamaIndex?
12. Explain the complete RAG pipeline.
