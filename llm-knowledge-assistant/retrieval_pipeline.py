from sentence_transformers import SentenceTransformer
import faiss

class RetrievalEngine:
    def __init__(self, docs):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.doc_map = {i: doc for i, doc in enumerate(docs)}
        self.embeddings = self.model.encode(docs)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def search(self, query, k=3):
        query_embed = self.model.encode([query])
        D, I = self.index.search(query_embed, k)
        return [self.doc_map[i] for i in I[0]]

    def format_prompt(self, query, context_docs):
        context = "\n".join(f"- {doc}" for doc in context_docs)
        return f"""
You are a helpful assistant. Use the context below to answer the user query.

Context:
{context}

User Question: {query}
Answer:"""
