import os
from dotenv import load_dotenv

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from groq import Groq

# Load environment variables
load_dotenv()

VECTOR_STORE_DIR = "data/vector_store"


# -------------------------
# Load Embedding Model
# -------------------------
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# -------------------------
# Load FAISS Vector Store
# -------------------------
def load_vector_store(embeddings):
    return FAISS.load_local(
        VECTOR_STORE_DIR,
        embeddings,
        allow_dangerous_deserialization=True
    )


# -------------------------
# Prompt Builder
# -------------------------
def build_prompt(context, question):
    return f"""
You are a senior digital design professor specializing in Verilog and VHDL.

Rules:
- Use ONLY the provided context.
- Explain concepts clearly and technically.
- If Verilog or VHDL is involved, mention syntax rules explicitly.
- Use bullet points where appropriate.
- If the answer is not in the context, say:
  "This is not explicitly covered in the provided textbooks."

Context:
{context}

Question:
{question}

Answer format:
- Definition
- Key differences or principles
- Example (if applicable)
""".strip()


# -------------------------
# Query Engine (SAFE)
# -------------------------
def ask_question(question: str, k: int = 5):
    # 🔐 HARD GUARD — NEVER allow None
    if question is None or not isinstance(question, str) or not question.strip():
        return "Please enter a valid question."

    question = question.strip()

    embeddings = load_embeddings()
    db = load_vector_store(embeddings)

    docs = db.similarity_search(question, k=k)
    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = build_prompt(context, question)

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=600
    )

    return response.choices[0].message.content.strip()


# -------------------------
# CLI Test
# -------------------------
if __name__ == "__main__":
    print("\nHDL Chatbot (RAG + Groq)")
    print("-" * 40)

    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break

        print("\nAnswer:\n", ask_question(q))
