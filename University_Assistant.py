import os
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Gemini API
API_KEY = "Your api"
GEMINI_EMBED_URL = f"https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedText?key={API_KEY}"
GEMINI_CHAT_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""

pdfs_directory = 'chat-with-pdf/pdfs/'
os.makedirs(pdfs_directory, exist_ok=True)

documents_store = []

def get_gemini_embedding(text):
    headers = {"Content-Type": "application/json"}
    body = {"text": text}
    response = requests.post(GEMINI_EMBED_URL, headers=headers, json=body)
    result = response.json()

    try:
        return np.array(result["embedding"]["value"])
    except:
        return None

def answer_question_with_gemini(question, context):
    prompt = template.format(question=question, context=context)

    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_CHAT_URL, headers=headers, json=body)
    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Sorry, I couldn't generate a response."

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())

def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    return loader.load()

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    return text_splitter.split_documents(documents)

def index_documents(chunks):
    for chunk in chunks:
        text = chunk.page_content
        embedding = get_gemini_embedding(text)
        if embedding is not None:
            documents_store.append({"content": text, "embedding": embedding})

def retrieve_relevant_docs(query, top_k=3):
    query_embedding = get_gemini_embedding(query)
    if query_embedding is None or not documents_store:
        return []

    similarities = []
    for doc in documents_store:
        sim = cosine_similarity([query_embedding], [doc["embedding"]])[0][0]
        similarities.append((sim, doc["content"]))

    similarities.sort(reverse=True)
    return [doc for _, doc in similarities[:top_k]]
