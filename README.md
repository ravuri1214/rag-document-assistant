# Intelligent Document Assistant (RAG)

## Overview

A Retrieval-Augmented Generation (RAG) system that enables semantic search and question answering over a collection of documents.

## Problem

Traditional keyword search fails to retrieve relevant information from unstructured documents, leading to poor answer quality.

## Solution

This project uses embeddings and vector search to retrieve relevant context and generate accurate responses using an LLM.

## Tech Stack

Python, LangChain, OpenAI, PostgreSQL (pgvector), FastAPI, Docker

## Workflow

1. Ingest documents
2. Split into chunks
3. Generate embeddings
4. Store in vector database
5. Retrieve relevant chunks
6. Generate response using LLM

## Results / Observations

* Improved retrieval relevance compared to keyword search
* Reduced hallucination using grounded context
* Tuned chunk size to improve answer accuracy

## ▶️ Run Locally

```bash
pip install -r requirements.txt
python app/main.py
```


