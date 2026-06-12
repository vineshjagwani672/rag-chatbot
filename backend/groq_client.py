import requests


def llama_chat(messages, api_key: str, model_name: str):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model_name,
        "messages": messages,
        "temperature": 0.4,
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as exc:
        return f"⚠️ Groq API Error:\n{str(exc)}"
