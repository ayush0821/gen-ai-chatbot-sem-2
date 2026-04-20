# config.py
# ─────────────────────────────────────────────────────────
# Get your FREE Groq API key from: https://console.groq.com
# ─────────────────────────────────────────────────────────


COLLEGE_NAME = "Shoolini university"
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
