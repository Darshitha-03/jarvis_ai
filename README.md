# Jarvis AI – Local RAG-Based Assistant

A locally hosted AI assistant that answers user queries based on custom documents using Retrieval-Augmented Generation (RAG). Supports both text and scanned PDF documents via OCR.

---

## Features

-  Document ingestion (TXT and PDF)
-  Semantic search using vector embeddings
-  Context-aware response generation using LLM
-  Interactive web interface (Flask + JavaScript)
-  OCR support for scanned PDFs using Tesseract
-  Persistent vector storage using ChromaDB

---

##  Tech Stack

- Python
- Flask
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- HuggingFace Inference API
- Tesseract OCR
- Poppler (PDF processing)
- HTML, CSS, JavaScript

---

##  How It Works

1. Documents are loaded and split into smaller chunks
2. Each chunk is converted into embeddings
3. Stored in ChromaDB vector database
4. On user query:
   - Relevant chunks are retrieved
   - Passed as context to LLM
   - Final answer generated

---

##  Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Darshitha-03/jarvis_ai.git
cd jarvis_ai