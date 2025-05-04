# 🧠 Local LLM Knowledge Assistant for Support Teams

A fully offline, lightweight AI assistant built to help internal support teams query technical documentation, logs, and SOPs using a quantized LLaMA 2 model. Includes semantic search with FAISS and SentenceTransformers, and interactive interfaces using FastAPI and Streamlit.

---

## 🚀 Features

* **Offline-first**: Uses quantized LLaMA 2 (4-bit GGUF) via `llama-cpp`
* **Semantic search**: Powered by `FAISS` and `SentenceTransformers`
* **Interactive REPL tools**: Shell commands, log parsing via LangChain Agents
* **Modern interfaces**: FastAPI (backend API) + Streamlit (frontend UI)
* **Live context memory**: REPL history and prompt summaries

---

## 📂 Folder Structure

```
llm-knowledge-assistant/
├── models/                  # LLaMA GGUF model file goes here
├── data/                    # Text documents for indexing (SOPs, logs)
│   ├── network_sop.txt
│   ├── device_reset.txt
│   └── log_snippet.txt
├── backend/
│   ├── main.py              # FastAPI app
│   ├── model_runner.py      # llama-cpp wrapper
│   ├── vector_store.py      # FAISS + SentenceTransformer
│   └── utils.py
├── frontend/
│   └── streamlit_app.py     # Streamlit frontend
├── requirements.txt         # All dependencies
├── Dockerfile
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/llm-knowledge-assistant.git
cd llm-knowledge-assistant
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Quantized Model

* Visit: [https://huggingface.co/TheBloke/LLaMa-2-7B-GGUF](https://huggingface.co/TheBloke/LLaMa-2-7B-GGUF)
* Download: `llama-2-7b-chat.Q4_0.gguf`
* Place it in the `models/` folder

---

## 🚀 Run the Application

### ✅ Start Backend (FastAPI)

```bash
uvicorn backend.main:app --reload --port 8000
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🔁 Start Frontend (Streamlit)

```bash
streamlit run frontend/streamlit_app.py
```

---

## 🔎 Example Interaction

**Prompt**: *"How do I restart the network?"*

**Retrieved Docs**:

```
To restart networking services on Linux:
1. sudo systemctl restart NetworkManager
2. sudo systemctl restart network.service
```

**LLM Output**:

```
To restart the network, run:
sudo systemctl restart NetworkManager
Use: systemctl status NetworkManager to verify.
```

---

## 🔍 Powered By

* LLaMA.cpp (GGUF model runner)
* LangChain (agent + tools)
* FAISS (vector DB)
* SentenceTransformers (embeddings)
* FastAPI (backend API)
* Streamlit (frontend UI)

---

## 📌 To-Do

* [ ] Add chat history context
* [ ] Dockerize for deployment
* [ ] Implement file upload interface

---

## 👨‍💼 Author

**Vijay Manjunath**
AI + Systems Engineer
[GitHub](https://github.com/YOUR_USERNAME) | [LinkedIn](https://linkedin.com/in/YOUR_LINK)
