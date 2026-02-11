from fastapi import FastAPI
from pydantic import BaseModel
from rules import match_rule
from memory import get_memory

app = FastAPI(title="Life Partner Rule-Based Chatbot")

class ChatRequest(BaseModel):
    session_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    end: bool = False


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    memory = get_memory(req.session_id)
    reply, action = match_rule(req.message, memory)

    return ChatResponse(
        reply=reply,
        end=True if action == "EXIT" else False
    )


@app.get("/")
def root():
    return {"status": "Chatbot is running 🚀"}
