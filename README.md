# 📚 AI Technical Interview Preparation Assistant

An AI-powered Technical Interview Preparation Assistant built using **LangGraph**, **LangChain**, **Mistral AI**, and **FAISS**. The application automatically classifies interview questions into different Computer Science subjects and retrieves relevant answers from PDF study materials using Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

- 📖 PDF-based knowledge retrieval using FAISS Vector Database
- 🤖 AI-powered question classification
- 🧠 Uses Mistral AI LLM for intelligent responses
- 🔍 Retrieval-Augmented Generation (RAG)
- 📂 Supports multiple Computer Science subjects:
  - Object-Oriented Programming (OOP)
  - Operating Systems (OS)
  - Computer Networks (CN)
  - Database Management Systems (DBMS)
- ⚡ Built using LangGraph workflow
- 💬 Interactive command-line chatbot

---

## 🛠️ Tech Stack

- Python
- LangChain
- LangGraph
- Mistral AI
- FAISS
- HuggingFace Embeddings
- PyPDFLoader
- python-dotenv

---

## 📁 Project Structure

```
AI-Technical-Interview-Assistant/
│
├── main.py
├── .env
├── requirements.txt
│
├── PDFs/
│   ├── Object Oriented Programming.pdf
│   ├── Operating System Notes.pdf
│   ├── Computer Networking Notes.pdf
│   └── DBMS Notes.pdf
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Technical-Interview-Assistant.git

cd AI-Technical-Interview-Assistant
```

### 2. Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` File

```env
MISTRAL_API_KEY=your_mistral_api_key
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 💡 How It Works

1. Loads PDF notes for all supported subjects.
2. Splits documents into smaller chunks.
3. Creates embeddings using HuggingFace.
4. Stores embeddings in a FAISS vector database.
5. Accepts a technical interview question.
6. Uses Mistral AI to classify the question into:
   - OOP
   - Operating Systems
   - Computer Networks
   - DBMS
7. Retrieves the most relevant document chunks.
8. Generates an accurate answer using Retrieval-Augmented Generation (RAG).

---

## 📚 Supported Subjects

- Object-Oriented Programming
- Operating Systems
- Computer Networks
- Database Management Systems

---

## 🧠 Workflow

```
User Question
      │
      ▼
Question Classifier
      │
      ▼
Select Subject
      │
      ▼
Retrieve Relevant PDF Chunks
      │
      ▼
Generate Response using Mistral AI
      │
      ▼
Return Answer
```

---

## 📦 Required Libraries

```text
langchain
langgraph
langchain-community
langchain-mistralai
langchain-huggingface
faiss-cpu
sentence-transformers
python-dotenv
pypdf
```

Install everything using:

```bash
pip install -r requirements.txt
```

---

## 📸 Example

```
Welcome to the Technical Interview Prep

Which subject you want to ask the questions

1. OOPS
2. OS
3. CN
4. DBMS

Enter 1,2,3 or 4: 2

Great! You can ask OS Technical Questions.

You: What is deadlock?

Assistant:
A deadlock is a situation where two or more processes are unable to proceed because each is waiting for resources held by the others...
```

---

## 🎯 Future Improvements

- Streamlit Web Interface
- Voice-based Interview Practice
- Multi-PDF Upload
- Conversation Memory
- Interview Quiz Mode
- Resume-Based Interview Questions
- MCQ Generation
- PDF Summarization
- Chat History Storage

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---



## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
