import streamlit as st

from backend.config import MODEL_NAME, PDF_PATH
from backend.pdf_service import clear_pdf_cache, get_pdf_info, load_chunks
from backend.rag_service import get_answer
from frontend.styles import APP_STYLES


WELCOME_MESSAGE = "Assalam o Alaikum! 👋 Main V&K ka Chatbot hoon. Jo bhi poochna hai bindaas poochho, main hoon na aapki madad ke liye."


def setup_page():
    st.set_page_config(
        page_title="Vinesh ka Chatbot 🤖",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(APP_STYLES, unsafe_allow_html=True)


def render_sidebar(pdf_info, pdf_chunks):
    with st.sidebar:
        st.markdown("## ⚡ V&K Assistant")
        st.markdown("""
        <div class="info-card">
            <b>Premium AI Chat Experience</b><br><br>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Features")
        st.markdown("""
        <span class="badge">PDF RAG</span>
        <span class="badge">Groq Powered</span>
        <span class="badge">Fast Replies</span>
        <span class="badge">Stylish UI</span>
        """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("""
        <div class="info-card">
            <b>Model:</b> {model_name}<br>
            <b>Status:</b> Ready to help 💬<br>
            <b>PDF:</b> vinesh_manual.pdf<br>
            <b>Updated:</b> {updated_at}<br>
            <b>Chunks:</b> {chunk_count}
        </div>
        """.format(
            model_name=MODEL_NAME,
            updated_at=pdf_info["updated_at"],
            chunk_count=len(pdf_chunks),
        ), unsafe_allow_html=True)

        if st.button("🔄 Reload PDF"):
            clear_pdf_cache()
            st.rerun()

        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = [{"role": "assistant", "content": WELCOME_MESSAGE}]
            st.rerun()


def render_header():
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">🤖 V&K ka Chatbot</div>
        <div class="hero-subtitle">
            Assalam o Alaikum! Ek modern, stylish aur intelligent chatbot experience —
        </div>
    </div>
    """, unsafe_allow_html=True)


def init_chat_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": WELCOME_MESSAGE}]


def render_messages():
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            avatar = "🤖" if message["role"] == "assistant" else "🧑"
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])


def handle_user_input(pdf_chunks):
    user_input = st.chat_input("Apna sawal likho...")

    if not user_input:
        return

    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Soch raha hoon..."):
            answer = get_answer(
                question=user_input,
                history=st.session_state.messages,
                pdf_chunks=pdf_chunks,
                api_key=st.secrets["GROQ_API_KEY"],
            )
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})


def run():
    setup_page()
    pdf_info = get_pdf_info(PDF_PATH)
    pdf_chunks = load_chunks(PDF_PATH, pdf_info["mtime_ns"], pdf_info["size"])

    render_sidebar(pdf_info, pdf_chunks)
    render_header()
    init_chat_state()
    render_messages()
    handle_user_input(pdf_chunks)
