from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sample_docs import documents

vectorizer = TfidfVectorizer()
doc_texts = [doc["content"] for doc in documents]
doc_vectors = vectorizer.fit_transform(doc_texts)

def get_answer(query: str):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, doc_vectors).flatten()
    best_index = scores.argmax()
    best_doc = documents[best_index]

    return {
        "answer": best_doc["content"],
        "source": best_doc["title"],
        "score": round(float(scores[best_index]), 4)
    }
