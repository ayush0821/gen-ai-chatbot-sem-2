# config.py
# ─────────────────────────────────────────────────────────
# Get your FREE Groq API key from: https://console.groq.com
# ─────────────────────────────────────────────────────────

#GROQ_API_KEY = "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"   # 🔑 Replace this!

COLLEGE_NAME = "Shoolini university"
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")