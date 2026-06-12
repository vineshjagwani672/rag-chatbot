import datetime
import os
import re

import pdfplumber
import streamlit as st


def get_pdf_info(pdf_path: str):
    stat = os.stat(pdf_path)
    return {
        "path": pdf_path,
        "size": stat.st_size,
        "mtime_ns": stat.st_mtime_ns,
        "updated_at": datetime.datetime.fromtimestamp(stat.st_mtime).strftime("%d %b %Y, %I:%M %p"),
    }


@st.cache_data
def load_chunks(pdf_path: str, pdf_mtime_ns: int, pdf_size: int, max_chars: int = 600):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tx = page.extract_text()
            if tx:
                text += tx + "\n"

    raw_parts = [p.strip() for p in text.split("\n") if p.strip()]
    chunks = []
    buf = ""

    for part in raw_parts:
        if len(buf) + len(part) <= max_chars:
            buf += " " + part
        else:
            chunks.append(buf.strip())
            buf = part

    if buf:
        chunks.append(buf.strip())

    return chunks


def clear_pdf_cache():
    load_chunks.clear()


def tokenize(text: str):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve_context(query: str, pdf_chunks, top_k: int = 3):
    q_words = tokenize(query)
    scored = []

    for chunk in pdf_chunks:
        chunk_words = tokenize(chunk)
        score = len(q_words & chunk_words)
        if score > 0:
            scored.append((score, chunk))

    if not scored:
        return ""

    scored.sort(reverse=True, key=lambda item: item[0])
    return "\n\n".join([chunk for _, chunk in scored[:top_k]])
