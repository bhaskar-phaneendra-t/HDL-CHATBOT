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
-  Railway (maintain my Mysql database)

---

##  Live Demo

(https://hdl-chatbot-bhasphanikarindra3.streamlit.app/)

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

# Local Setup Guide
---
## Step 0
###  Project Folder Structure
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

## Step 1: Download texbook pdfs
Instead of HDL related texbook pdf you can use any textbook pdf.
``` markdown
├── data/
│   ├── pdfs/
|       |──(store them here)
```
## Step 2: Create Virtual Environment
```bash
python -m venv projectenv
projectenv\Scripts\activate
```
## Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## Step 4: Create .env file
this file stores all the private information of the project that should not be shared
```ini
GROQ_API_KEY=your_groq_key
HF_API_KEY=your_hf_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
MYSQL_URL=your_mysql_connection_string
```

>  **Never upload `.env` to GitHub.**

##Step 5: Ingest HDL Textbooks
```bash
python -m rag.ingest

```
This builds the FAISS vector store.

##Step 6: Run the App
```bash
streamlit run app.py
```
this will make you open the browser with 
```arduino
http://localhost:8501
```

This is the part that ends up to local working chatbot

# Deployment Guide

## Deploy this in Streamlit Cloud.

## Step 1:
push this into Git repo.

## Step 2:
click on this link (https://streamlit.io/cloud)

## Step 3:
create a new app and select the repo of Git.

## Step 4:
select main file as app.py and then deploy.

## Step 5:
In deployed streamlit redirect to

```nginx
App → Settings → Secrets
```
## Step 6:
Add your .env file contents here.

## Step 7:
In local file google_auth.py replace the lilnk that you produced in streamlit deployment

## Step 8:
Add this url in OAuth 2.0 Client ID also.

(https://console.cloud.google.com/)

```nginx
APIs & Services → Credentials → OAuth 2.0 Client ID → Authorized Redirect URIs
```

## Step 9:
Make sure the database Railway MySQL is not internal and public.

## Step 10:
Once reboot the deployment.

#Knowledge Base
This chatbot uses the following textbooks as its retrieval source:
- Digital Design & Computer Architecture
- Verilog HDL – Samir Palnitkar
- VHDL Programming by Example
- HDL Lecture Notes
You can replace these with any PDF textbooks of your choice.

# Security Notes
- .env file is ignored via .gitignore
- OAuth tokens are not hardcoded
- Secrets are managed through Streamlit Cloud
- MySQL credentials are never exposed in code
- 

##  Author
**Tatapudi Bhaskar Phaneendra**
