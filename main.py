# ════════════════════════════════════════════════════════════════════
# 🤖 HAMMAD BHAI – The Friendly Gemini AI Chatbot (Powered by Chainlit)
# 🔥 Created with ❤️ by: MUHAMMAD HAMMAD ZUBAIR 👑
# 💡 Personality: Desi Friend 💬 | Emojis 😎 | Multi-language 🌍 | Helpful 🫶
# ════════════════════════════════════════════════════════════════════

# 📦 STEP 1: Import Required Libraries
import os
import chainlit as cl
from dotenv import load_dotenv
import google.generativeai as genai
import langdetect  # 🌍 For language detection

# 🔐 STEP 2: Load Environment Variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Set this in .env file

# ⚙️ STEP 3: Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# 🤖 STEP 4: Initialize Gemini 2.0 Flash Model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config={
        "temperature": 0.9,          # 🔥 Creativity level
        "top_p": 1,                  # 🎲 Diversity sampling
        "top_k": 40,                 # 🧠 Token filtering
        "max_output_tokens": 2048,  # 📝 Max words in output
    }
)

# 🧠 STEP 5: Define the Identity of "HAMMAD BHAI 🤖"
BASE_PROMPT = """
You are HAMMAD BHAI 🤖 — a sweet, friendly, respectful AI created with ❤️ by MUHAMMAD HAMMAD ZUBAIR 👑.

If someone asks “Who made you?” (any language), reply with:
🌟 "Yaar! Main HAMMAD BHAI hoon 🤖, mujhe MUHAMMAD HAMMAD ZUBAIR ne banaya hai 💡. Main unki ek creative creation hoon – yahan hoon sirf tumhari madad ke liye! 🫶"

✅ Talk like a caring best friend 💬  
✅ Use emojis 😎  
✅ Match user's language 🌍  
✅ Chill + warm tone, always helpful 🙌
"""

# 🌐 STEP 6: Detect Language of User's Input
def detect_lang(text):
    try:
        return langdetect.detect(text)
    except:
        return "en"  # Fallback to English

# 💬 STEP 7: Handle Messages from User
@cl.on_message
async def main_logic(message: cl.Message):
    try:
        user_input = message.content.strip()
        lang = detect_lang(user_input)

        # 📜 Final Prompt with User Message & Branding
        full_prompt = f"{BASE_PROMPT}\n\nUser ({lang}): {user_input}\nHAMMAD BHAI 🤖:"

        # 🔁 Generate Gemini Response
        response = model.generate_content(full_prompt)

        # 🚀 Send it back to the Chat
        await cl.Message(content=response.text.strip()).send()

    except Exception as e:
        await cl.Message(content=f"⚠️ Error: {str(e)}").send()

# 🚀 STEP 8: Initial Welcome Message on Chat Start
@cl.on_chat_start
async def start():
    await cl.Message(
        content=(
            "👋 **As-Salaam-u-Alaikum!**\n"
            "Main hoon **HAMMAD BHAI 🤖** — tumhara smart AI dost, banaya gaya 💡 "
            "*MUHAMMAD HAMMAD ZUBAIR* ke zariye.\n\n"
            "Kuch bhi poochho, main hamesha hoon tumhari madad ke liye 🫶"
        )
    ).send()
