# llm-knowledge-assistant/model_runner.py
from llama_cpp import Llama

llm = Llama(
    model_path="/content/models/llama-2-7b-chat.Q4_0.gguf",  # adjust path if needed
    n_ctx=2048,
    n_threads=6,
    n_gpu_layers=40,
)

def run_llm(prompt):
    output = llm(prompt=prompt, max_tokens=200, stop=["</s>"])
    return output["choices"][0]["text"].strip()
