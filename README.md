# 🤖 HDL-CHATBOT  
## HDL Chatbot – RAG-based Verilog & VHDL Assistant

An AI-powered HDL (Hardware Description Language) chatbot built using Retrieval-Augmented Generation (RAG) to answer Verilog and VHDL questions using textbook knowledge.

---

## 🚀 Tech Stack

- 🧠 RAG (Retrieval-Augmented Generation)
- 📚 Verilog & VHDL textbooks as knowledge base
- ⚡ Groq LLM API (llama-3.1-8b-instant)
- 🔎 HuggingFace Embeddings + FAISS
- 🔐 Google OAuth Login
- 🗄 MySQL (Railway) for persistent chat history
- 🎨 Streamlit UI

---

## 🌐 Live Demo

👉 (Insert your Streamlit Cloud URL here)

---

## ✨ Features

- ✅ Google Login Authentication
- ✅ Multi-chat support
- ✅ Persistent chat history (MySQL)
- ✅ Auto chat renaming based on first question
- ✅ Retrieval from HDL textbooks
- ✅ Context-aware responses
- ✅ Clean dark-mode UI
- ✅ Production-ready structure
- ✅ Secure secret handling

---

## 🏗 Architecture Overview

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


---

## 📂 Project Structure

GEN_AI/
│
├── app.py # Main Streamlit application
├── requirements.txt
├── .gitignore
│
├── auth/ # Google OAuth logic
├── db/ # MySQL models + CRUD operations
├── rag/ # RAG pipeline
│ ├── ingest.py
│ ├── embeddings.py
│ ├── query_engine.py
│ └── vector_store.py
│
├── data/
│ ├── pdfs/ # HDL textbooks
│ └── vector_store/ # FAISS index


---

## ⚙️ Local Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/hdl-chatbot.git
cd hdl-chatbot
2️⃣ Create Virtual Environment
python -m venv projectenv
projectenv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create .env File
Create a file named .env in the root directory and add:

GROQ_API_KEY=your_groq_key
HF_API_KEY=your_hf_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
MYSQL_URL=your_mysql_connection_string
⚠ Never upload .env to GitHub.

5️⃣ Ingest HDL Textbooks
python -m rag.ingest
This builds the FAISS vector store.

6️⃣ Run the App
streamlit run app.py
Open the browser at:

http://localhost:8501
🌍 Deployment (Streamlit Cloud)
Push repository to GitHub

Go to https://share.streamlit.io

Deploy repository

Add secrets in Streamlit Cloud:

GROQ_API_KEY = "your_key"
HF_API_KEY = "your_key"
GOOGLE_CLIENT_ID = "your_id"
GOOGLE_CLIENT_SECRET = "your_secret"
MYSQL_URL = "your_mysql_url"
Update Google OAuth Redirect URI:

https://your-app-name.streamlit.app/
📚 Knowledge Base
The chatbot retrieves context from:

📘 Digital Design & Computer Architecture

📗 Verilog HDL – Samir Palnitkar

📙 VHDL Programming by Example

📄 HDL Lecture Notes

Responses are generated using retrieved textbook context only.

🔐 Security Notes
.env ignored via .gitignore

OAuth credentials stored securely

No API keys committed to GitHub

MySQL hosted securely on Railway

Production secrets handled via Streamlit Cloud

🛠 Future Improvements
⏳ Streaming token responses

📌 Source citation display

🗑 Chat delete feature

✏ Manual rename feature

📊 Admin analytics dashboard

🧠 Per-chat memory enhancement

🌍 Custom domain support

👨‍💻 Author
Bhaskar Phaneendra
AI / Full-Stack Developer
