from fastapi import FastAPI
from pydantic import BaseModel
import random
from rules import match_rule_english, match_rule_urdu
from memory import get_memory

app = FastAPI(title="Casual Life Partner Chatbot")

# ----------------- Models -----------------
class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    end: bool = False


# ----------------- GET Endpoint (first prompt) -----------------
@app.get("/chat", response_model=ChatResponse)
def chat_get():
    # This runs automatically when you open /chat in the browser
    return ChatResponse(
        reply="Welcome! 🌟 I’m here to chat with you about your life partner. Please choose your preferred language: English or Urdu.",
        end=False
    )


# ----------------- POST Endpoint (conversation) -----------------
@app.post("/chat", response_model=ChatResponse)
def chat_post(req: ChatRequest):
    memory = get_memory(req.session_id)
    msg = req.message.strip().lower()

    # First-time entry: no language chosen yet
    if getattr(memory, "language", None) is None:
        if msg == "english":
            memory.language = "english"
            replies = [
                "Wonderful! 💫 We’ll continue in English. How are you feeling right now?",
                "Wonderful choice! 💖 Tell me — how’s your heart today?",
                "English it is! 🌟 Let’s begin with something simple — how are you doing?"
            ]
            return ChatResponse(reply=random.choice(replies), end=False)

        elif msg == "urdu":
            memory.language = "urdu"
            return ChatResponse(
                reply="خوش آمدید! 🌸 آپ اردو چیٹ میں ہیں۔ آئیے بات شروع کریں — آج آپ کیسا محسوس کر رہے ہیں؟",
                end=False
            )

        else:
            return ChatResponse(
                reply="Please choose a language first: English or Urdu",
                end=False
            )

    # Route to rules once language is chosen
    if memory.language == "english":
        reply, action = match_rule_english(msg, memory)
    elif memory.language == "urdu":
        reply, action = match_rule_urdu(msg, memory)
    else:
        reply, action = "Language not recognized. Please choose English or Urdu.", None

    # Save last message for continuity
    memory.last_message = msg

    return ChatResponse(
        reply=reply,
        end=True if action == "EXIT" else False
    )


# ----------------- Root Endpoint -----------------
@app.get("/")
def root():
    return {"status": "Chatbot is running 🚀"}
