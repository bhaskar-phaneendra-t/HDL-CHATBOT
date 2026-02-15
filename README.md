#  HDL-CHATBOT  
## HDL Chatbot – RAG-based Verilog & VHDL Assistant

An AI-powered HDL (Hardware Description Language) chatbot built using Retrieval-Augmented Generation (RAG) to answer Verilog and VHDL questions using textbook knowledge.

---

##  Tech Stack

-  RAG (Retrieval-Augmented Generation)
-  Verilog & VHDL textbooks as knowledge base
-  Groq LLM API (llama-3.1-8b-instant)
-  HuggingFace Embeddings + FAISS
-  Google OAuth Login
-  MySQL (Railway) for persistent chat history
-  Streamlit UI

---

##  Live Demo

👉 (Insert your Streamlit Cloud URL here)

---

##  Features

-  Google Login Authentication
-  Multi-chat support
-  Persistent chat history (MySQL)
-  Auto chat renaming based on first question
-  Retrieval from HDL textbooks
-  Context-aware responses
-  Clean dark-mode UI
-  Production-ready structure
-  Secure secret handling

---

##  Architecture Overview
```markdowm
User
↓
Streamlit UI
↓
Google OAuth
↓
MySQL (User + Chat Storage)
↓
RAG Pipeline
├── FAISS Vector Store
├── HuggingFace Embeddings
└── Groq LLM
↓
AI Response

```

## Local Setup Guide
---
### Step 1
##  Project Structure
```markdown
hdl-chatbot/
│
├── app.py                     # Streamlit entry point
│
├── auth/
│   ├── google_auth.py
│   └── session.py
│
├── rag/
│   ├── ingest.py              # PDF → embeddings (one-time)
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── prompt.py
│
├── chat/
│   ├── chat_engine.py
│   ├── memory.py
│   └── history.py
│
├── db/
│   ├── mysql.py
│   ├── models.py
│   └── queries.py
│
├── ui/
│   ├── login.py
│   ├── chat_ui.py
│   └── sidebar.py
│
├── config/
│   ├── settings.py
│   └── secrets.toml
│
├── data/
│   ├── pdfs/
│   └── vector_store/
│
├── requirements.txt
└── README.md

```



