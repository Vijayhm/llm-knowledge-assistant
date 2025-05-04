# llm-knowledge-assistant/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from query_engine import FAISSQueryEngine
from model_runner import run_llm

app = FastAPI()
engine = FAISSQueryEngine(
    index_path="/content/data/faiss_index.idx",
    meta_path="/content/data/index_meta.pkl"
)

class AskRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(req: AskRequest):
    docs = engine.search(req.query)
    context = "\n".join(docs)
    prompt = f"""You are a helpful assistant. Use the context below to answer the user query.

Context:
{context}

User Question: {req.query}
Answer:"""
    answer = run_llm(prompt)
    return {"answer": answer, "source_docs": docs}
