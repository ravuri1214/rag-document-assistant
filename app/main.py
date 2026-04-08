from fastapi import FastAPI
from retriever import get_answer

app = FastAPI(title="RAG Document Assistant")

@app.get("/")
def home():
    return {"message": "RAG Document Assistant API is running"}

@app.get("/ask")
def ask(query: str):
    result = get_answer(query)
    return {
        "query": query,
        "answer": result["answer"],
        "source": result["source"],
        "similarity_score": result["score"]
    }
