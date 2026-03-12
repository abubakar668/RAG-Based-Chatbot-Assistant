# RAG-Based University Assistant Chatbot

This is an AI chatbot that helps university students by answering their questions using uploaded PDF files. It uses a method called RAG (Retrieval-Augmented Generation) and Google's Gemini API to find answers from the document.

## Project Goal

Many students ask the same questions again and again on WhatsApp, Instagram, and YouTube which gets hard to answer. This chatbot gives automatic answers to help solve that problem.

## How It Works

1. Upload a PDF file (for example: university FAQs).
2. The chatbot reads and splits the content into small parts.
3. You type a question (for example: "What documents are needed for NTS?").
4. The chatbot finds the most relevant parts from the PDF.
5. It uses those parts to give a short and correct answer.

### How to run this
### 1. Clone the Repository
- git clone https://github.com/YOUR_USERNAME/RAG-Based-Chatbot-Assistant.git
- cd RAG-Based-Chatbot-Assistant

### 2. Install Libraries:
- pip install -r requirements.txt

### 3. Run the program:
- streamlit run University_Assistant.py
