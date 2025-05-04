import streamlit as st
import requests

# Set FastAPI endpoint (replace with ngrok public URL if on Colab)
API_URL = "http://127.0.0.1:8000/ask"  # Or ngrok URL like https://abc123.ngrok.io/ask

st.set_page_config(page_title="LLM Knowledge Assistant", layout="centered")

st.title("📚 Local LLM Knowledge Assistant")
st.markdown("Ask a question based on your uploaded documents!")

query = st.text_input("🔍 Enter your question:", placeholder="e.g. How do I restart the network service?")

if st.button("Ask") and query:
    with st.spinner("🧠 Thinking..."):
        try:
            res = requests.post(API_URL, json={"query": query})
            res.raise_for_status()
            data = res.json()
            st.subheader("📝 Answer")
            st.write(data.get("answer", "No answer found."))

            if "source_docs" in data:
                st.subheader("📎 Source Documents")
                for doc in data["source_docs"]:
                    st.code(doc, language="text")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
