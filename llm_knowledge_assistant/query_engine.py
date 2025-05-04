# llm-knowledge-assistant/query_engine.py
import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

class FAISSQueryEngine:
    def __init__(self, index_path, meta_path):
        self.index = faiss.read_index(index_path)
        with open(meta_path, "rb") as f:
            self.meta = pickle.load(f)
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query, top_k=3):
        query_vector = self.embedder.encode([query])
        distances, indices = self.index.search(query_vector, top_k)
        results = [self.meta[i] for i in indices[0] if i != -1]
        return results
