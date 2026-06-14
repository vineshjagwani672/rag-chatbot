# 🤖 Pawan Vinesh Electronics – AI PDF Chatbot

> A Streamlit-based RAG chatbot that reads company documents and answers customer queries using Groq AI.

---

## 👨‍💻 Student Information

| Field | Details |
|-------|---------|
| **Name** | Vinesh Kumar |
| **Roll No** | 67928 |
| **Course** | Parallel & Distributed Computing (PDC) |
| **Project** | RAG-Based AI Chatbot |

---

## 🔗 Live Links

| Platform | Link |
|----------|------|
| 🤖 **AI Chatbot** | [Open Chatbot](https://rag-chatbot-6cytxsny2bdohfnohsujuk.streamlit.app/) |
| 🌐 **Website** | [Open Website](https://vineshjagwani672.github.io/rag-chatbot/) |
| 📁 **GitHub Repo** | [View Code](https://github.com/vineshjagwani672/rag-chatbot) |

---

## 📌 Project Overview

**Pawan Vinesh Electronics AI Chatbot** answers customer questions about products, prices, repairs, warranty, and payments — directly from the company's official PDF manual using RAG (Retrieval Augmented Generation) technology.

---

## ✅ Features

- PDF-based question answering
- Groq-powered chat responses
- Streamlit chat interface
- PDF cache refresh based on file update time and size
- Sidebar PDF status with chunk count
- Manual `Reload PDF` button
- Answers in English only

---

## 📂 Project Structure

```text
.
├── frontend/
│   └── index.html              ← Marketing landing page
├── backend/
│   └── data/
│       └── vinesh_manual.pdf   ← Company knowledge base
├── app.py                      ← Main Streamlit application
├── requirements.txt            ← Python dependencies
└── .streamlit/
    └── secrets.toml            ← API keys (not pushed to GitHub)
```

---

## ⚙️ How RAG Works (PDC Concept)

```
User Question
      ↓
PDF split into chunks  (distributed data)
      ↓
Chunks searched in parallel  (parallel processing)
      ↓
Relevant chunks retrieved
      ↓
Groq AI generates answer
      ↓
Answer displayed to user
```

> Each PDF chunk acts as a distributed data unit — search across chunks runs in parallel, making this a real-world PDC application.

---

## 🚀 Requirements

- Python 3.11+
- Groq API key

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔧 Setup

Create `.streamlit/secrets.toml` and add your Groq API key:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

> The secrets file is ignored by Git and must not be pushed to GitHub.

---

## ▶️ Run Locally

```bash
python -m streamlit run app.py
```

With virtual environment:

```bash
./venv/bin/python -m streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 📄 Update The PDF

Replace the file:

```
data/vinesh_manual.pdf
```

After updating:
1. Restart the app, or
2. Click `Reload PDF` in the sidebar

The app automatically refreshes cached chunks when PDF file size or modified time changes.

---

## ☁️ Deploy On Streamlit Cloud

1. Push changes to GitHub
2. Connect GitHub repo in Streamlit Cloud
3. Add `GROQ_API_KEY` in Streamlit Cloud secrets
4. Deploy from `app.py`

Streamlit Cloud auto-redeploys on every GitHub push.

---

## 📝 Notes

- Chatbot answers only from the PDF — company-specific information only
- If information is missing from PDF, chatbot asks user to update the PDF
- Do not commit `.streamlit/secrets.toml`, `venv/`, or `__pycache__/`

---

*Built with ❤️ by Vinesh Kumar | Roll No: 67928*
