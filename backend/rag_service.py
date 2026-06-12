import datetime

from backend.config import MODEL_NAME
from backend.groq_client import llama_chat
from backend.pdf_service import retrieve_context


def build_system_prompt(context: str):
    today = datetime.datetime.now().strftime("%d %B %Y (%Y)")
    pdf_strength = len(context.strip())

    if pdf_strength < 50:
        return f"""
You are Pawan Vinesh Electronics ka official chatbot. Only answer based on the PDF context provided. Do not use general knowledge for company-specific information.

Rules:
- Give clear and direct answers.
- Today is {today}.
- If the answer is not available in the PDF context, say that the PDF does not include this information and ask the user to upload/update the PDF.
- Do NOT say anything about "searching", "checking", "researching", or "not knowing".
- Never restrict information to the year 2023.
- Reply in a friendly, helpful style.
"""

    return f"""
You are Pawan Vinesh Electronics ka official chatbot. Only answer based on the PDF context provided. Do not use general knowledge for company-specific information.

Use the following PDF text as your main reference.
If updated information (today = {today}) is needed, include it naturally.

PDF Context:
---------------------
{context}
---------------------

Rules:
- Provide confident and direct answers.
- Do NOT say "I am searching" or "I am researching".
- Never limit your knowledge to only 2023.
- Keep the reply natural and user-friendly.
"""


def get_answer(question: str, history, pdf_chunks, api_key: str):
    context = retrieve_context(question, pdf_chunks)
    system_prompt = build_system_prompt(context)
    messages = [{"role": "system", "content": system_prompt}]

    for message in history[-6:]:
        messages.append(message)

    messages.append({"role": "user", "content": question})

    return llama_chat(messages, api_key=api_key, model_name=MODEL_NAME)
