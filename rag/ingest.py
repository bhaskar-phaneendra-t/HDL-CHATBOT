import os
from tqdm import tqdm
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS


from rag.chunking import get_text_splitter
from rag.embeddings import get_embedding_model
from rag.text_cleaner import clean_text

PDF_DIR = "data/pdfs"
VECTOR_STORE_DIR = "data/vector_store"

def load_pdfs():
    documents = []
    for file in os.listdir(PDF_DIR):
        if not file.lower().endswith(".pdf"):
            continue

        path = os.path.join(PDF_DIR, file)
        try:
            print(f"📄 Loading: {file}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"⚠️ Skipping corrupted PDF: {file}")
            print(f"   Reason: {e}")

    return documents


def ingest():
    print(" Loading PDFs...")
    raw_docs = load_pdfs()

    print(" Chunking documents...")
    splitter = get_text_splitter()
    chunks = splitter.split_documents(raw_docs)
    for chunk in chunks:
        chunk.page_content = clean_text(chunk.page_content)

    print(f" Total chunks created: {len(chunks)}")

    print(" Generating embeddings...")
    embeddings = get_embedding_model()

    print(" Building FAISS vector store...")
    vectorstore = FAISS.from_documents(
        tqdm(chunks),
        embedding=embeddings
    )

    vectorstore.save_local(VECTOR_STORE_DIR)
    print(" Vector store saved successfully!")

if __name__ == "__main__":
    ingest()
