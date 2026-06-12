# V&K PDF Chatbot

A Streamlit-based PDF chatbot for Pawan Vinesh Electronics. The app reads `data/vinesh_manual.pdf`, retrieves relevant PDF context, and answers user questions through the Groq chat completions API.

## Features

- PDF-based question answering
- Groq-powered chat responses
- Streamlit chat interface
- PDF cache refresh based on file update time and size
- Sidebar PDF status with chunk count
- Manual `Reload PDF` button

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── data/
│   └── vinesh_manual.pdf
└── .streamlit/
    └── secrets.toml
```

## Requirements

- Python 3.11+
- Groq API key

Install dependencies:

```bash
pip install -r requirements.txt
```

## Setup

Create `.streamlit/secrets.toml` and add your Groq API key:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

The secrets file is ignored by Git and should not be pushed to GitHub.

## Run Locally

From the project folder:

```bash
python -m streamlit run app.py
```

If you are using the included virtual environment:

```bash
./venv/bin/python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## Update The PDF

Replace this file with the new manual:

```text
data/vinesh_manual.pdf
```

After updating the PDF:

1. Restart the app, or
2. Click `Reload PDF` in the sidebar.

The app automatically refreshes cached PDF chunks when the PDF file size or modified time changes.

## Deploy On Streamlit Cloud

1. Push changes to GitHub.
2. Connect the GitHub repo in Streamlit Cloud.
3. Add `GROQ_API_KEY` in Streamlit Cloud app secrets.
4. Deploy the app from `app.py`.

When the connected GitHub branch is pushed, Streamlit Cloud should automatically redeploy the app.

## Notes

- The chatbot is designed to answer company-specific questions from the PDF.
- If the PDF does not include the requested information, the chatbot should ask the user to update or upload the correct PDF.
- Do not commit `.streamlit/secrets.toml`, `venv/`, or `__pycache__/`.
