# Jarvis AI – Document Intelligence System

Jarvis AI is a locally hosted web application that enables users to upload documents and query their content using natural language. The system is built using a retrieval-augmented generation (RAG) pipeline.

## Features

- Document ingestion (TXT, PDF, ODT)
- Automatic text extraction and chunking
- Semantic search using vector embeddings
- Context-aware response generation using a language model
- File-specific querying support
- Persistent vector storage using ChromaDB

## Architecture

Upload → Processing → Embedding → Storage → Retrieval → Response Generation

## Technology Stack

- Python
- Flask
- ChromaDB
- Hugging Face Inference API (Qwen 2.5)
- HTML, CSS, JavaScript

## Project Structure

jarvis_core/
- uploader.py
- retriever.py
- generator.py
- vector_store.py

templates/
static/
app.py

## Setup Instructions

1. Clone the repository

git clone https://github.com/Darshitha-03/jarvis_ai.git  
cd jarvis_ai

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000

## Usage

- Upload a document through the interface
- Ask questions related to the uploaded content
- The system retrieves relevant information and generates a response

## Notes

- Uploaded files are stored locally and not included in the repository
- The vector database is maintained locally
- Designed for single-user usage

## Future Work

- Multi-user support
- File management interface
- Improved retrieval ranking
- Streaming responses

## Author

Darshitha
