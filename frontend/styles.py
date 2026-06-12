APP_STYLES = """
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #111827 35%, #1f2937 100%);
    color: #f9fafb;
    font-family: 'Inter', sans-serif;
}

.main > div {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

[data-testid="stSidebar"] {
    background: rgba(17, 24, 39, 0.85);
    backdrop-filter: blur(12px);
    border-right: 1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] * {
    color: #f9fafb !important;
}

.hero-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.25), rgba(16,185,129,0.18));
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 24px;
    padding: 28px 30px;
    margin-bottom: 20px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.30);
    backdrop-filter: blur(14px);
}

.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 1rem;
    color: #d1d5db;
    line-height: 1.6;
}

[data-testid="stChatMessage"] {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 12px 14px;
    margin-bottom: 12px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.20);
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background: linear-gradient(135deg, rgba(79,70,229,0.20), rgba(59,130,246,0.10));
    border: 1px solid rgba(99,102,241,0.35);
}

[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background: linear-gradient(135deg, rgba(16,185,129,0.16), rgba(6,182,212,0.08));
    border: 1px solid rgba(16,185,129,0.28);
}

[data-testid="stChatInput"] {
    background: rgba(255,255,255,0.06);
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.08);
    padding: 6px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.22);
}

[data-testid="stChatInput"] textarea {
    color: white !important;
}

.stButton > button {
    background: linear-gradient(135deg, #6366f1, #14b8a6);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 1rem;
    box-shadow: 0 8px 18px rgba(0,0,0,0.25);
}

.stButton > button:hover {
    transform: translateY(-1px);
    transition: 0.2s ease;
    filter: brightness(1.05);
}

.info-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 16px;
    margin-bottom: 16px;
    backdrop-filter: blur(10px);
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    margin: 4px 6px 0 0;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    background: rgba(99,102,241,0.18);
    border: 1px solid rgba(99,102,241,0.35);
    color: #e5e7eb;
}

header[data-testid="stHeader"] {
    background: transparent;
}

p, li, div {
    color: #f3f4f6;
}

[data-testid="stSpinner"] * {
    color: #e5e7eb !important;
}
</style>
"""
