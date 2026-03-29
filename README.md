# RAG-Based University Assistant Chatbot

This is an AI chatbot that helps university students by answering their questions using uploaded PDF files. It uses a method called RAG (Retrieval-Augmented Generation) with local embeddings and Groq's Llama 3.1 model to find and generate answers from the document.

This chatbot was made as a project to help university students get quick answers to common questions.


## Project Goal

Many students ask the same questions again and again on WhatsApp, Instagram, and YouTube which gets hard to answer. This chatbot gives automatic answers to help solve that problem.


## Data Collection

To make this chatbot useful:

- I visited 20 different university websites in Pakistan and collected their FAQs (Frequently Asked Questions).
- I also gathered common student questions through a form.
- I combined all these questions and answers into one PDF.
- This PDF is used by the chatbot to answer questions.


## What This Chatbot Can Do

- Reads PDF files like brochures, admission guides, and FAQs.
- Understands student questions.
- Gives quick and smart answers using AI.


## Features

- Upload university-related PDF documents (e.g. university_faq.pdf)
- Breaks the PDF into small parts for better understanding.
- Turns those parts into embeddings locally using sentence-transformers (no external API needed for this step).
- Finds the best parts of the PDF related to your question using cosine similarity.
- Gives a short and helpful answer using Groq's Llama 3.1 model (free tier).
- Caches embeddings per PDF so re-uploads are instant.
- Easy-to-use web app made with Streamlit.


## Tools and Technologies Used

- Python
- LangChain
- Streamlit
- PDFPlumber
- NumPy & scikit-learn
- sentence-transformers (all-MiniLM-L6-v2) — local embeddings
- Groq API (Llama 3.1 8B) — answer generation


## How It Works

1. Upload a PDF file (for example: university FAQs).
2. The chatbot reads and splits the content into small parts.
3. Each part is converted into an embedding vector locally.
4. You type a question (for example: "What documents are needed for admission?").
5. The chatbot finds the most relevant parts from the PDF.
6. It sends those parts along with your question to Llama 3.1 via Groq to generate a concise answer.


## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/RAG-Based-Chatbot-Assistant.git
cd RAG-Based-Chatbot-Assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key

Get a free Groq API key from https://console.groq.com/keys

Copy the example env file and add your key:

```bash
cp .env.example .env
```

Then edit `.env` and replace `your-groq-api-key-here` with your actual key.

> **Note:** The `.env` file is gitignored and will never be pushed to GitHub.

### 4. Run the App

```bash
streamlit run University_Assistant.py
```

The app will open at http://localhost:8501


## Future Plans

- Add human support when the AI can't answer.
- Add voice support so users can speak their questions.
- Make a mobile app for easy access on phones.
- Add Urdu language support.


## Author

- Muhammad Abubakar
