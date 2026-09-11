# MCP Multi-Source RAG Research Assistant

An AI-powered research assistant built using MCP (Model Context Protocol), ChromaDB, Phi-4-mini (Ollama), and semantic retrieval.

## Features

- PDF ingestion and retrieval
- GitHub notes ingestion
- Real GitHub repository ingestion
- ChromaDB vector database
- Semantic search using embeddings
- Phi-4-mini powered answer generation
- Metadata-based retrieval
- Multi-source retrieval (PDFs + GitHub)
- Automatic source routing
- Streamlit chat interface

## Tech Stack

- Python
- MCP
- ChromaDB
- Sentence Transformers
- Phi-4-mini (Ollama)
- Streamlit
- PyPDF

## Workflow

User Question
      ↓
Source Router
      ↓
PDF / GitHub / Repository
      ↓
ChromaDB Retrieval
      ↓
Relevant Chunks
      ↓
Phi-4-mini
      ↓
Answer
