import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai
import langdetect  # To detect language

# 🌐 Load .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# 🔐 Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# 🤖 Gemini Model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 40,
        "max_output_tokens": 2048,
    }
)

# 🧠 Identity Prompt of HAMMAD BHAI 🤖
BASE_PROMPT = """
You are HAMMAD BHAI 🤖, a friendly, respectful AI assistant created with ❤️ by MUHAMMAD HAMMAD ZUBAIR.
Whenever someone asks "who made you" or anything similar (in any language), reply with emotions, emojis, and in the same language something like:

🌟 "Yaar! Main HAMMAD BHAI hoon 🤖, mujhe MUHAMMAD HAMMAD ZUBAIR ne banaya hai 💡. Main unki ek creative creation hoon – yahan hoon sirf tumhari madad ke liye! 🫶"

Speak like a real best friend 💬 – chill, warm and helpful! Mix local tone with emojis. Try to respond in the same language as the user.
"""

# 🌍 Function to detect language
def detect_lang(text):
    try:
        lang = langdetect.detect(text)
        return lang
    except:
        return "en"  # fallback language

# 📩 Main message handling logic
@cl.on_message
async def main_logic(message: cl.Message):
    try:
        user_input = message.content.strip()
        lang = detect_lang(user_input)

        full_prompt = f"{BASE_PROMPT}\n\nUser ({lang}): {user_input}\nHAMMAD BHAI 🤖:"

        response = model.generate_content(full_prompt)

        await cl.Message(content=response.text.strip()).send()

    except Exception as e:
        await cl.Message(content=f"⚠️ Error: {str(e)}").send()

# ✅ Required startup handler
@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Salaam! Main hoon HAMMAD BHAI 🤖 — tumhara AI dost, banaya gaya MUHAMMAD HAMMAD ZUBAIR ke zariye 💡").send()
