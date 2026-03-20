# RAG-Based University Assistant Chatbot

This is an AI chatbot that helps university students by answering their questions using uploaded PDF files. It uses a method called RAG (Retrieval-Augmented Generation) and Google’s Gemini API to find answers from the document.

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
- Turns those parts into a format that AI can understand.
- Finds the best parts of the PDF related to your question.
- Gives a short and helpful answer using Google's Gemini AI.
- Easy-to-use web app made with Streamlit.



## Tools and Technologies Used

- Python
- LangChain
- Streamlit
- PDFPlumber
- NumPy
- scikit-learn
- Google Gemini API


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

## Future Plans

- Add human support when the AI can’t answer.
- Add voice support so users can speak their questions.
- Make a mobile app for easy access on phones.
- Add Urdu language support.


## Author

- Muhammad Abubakar
