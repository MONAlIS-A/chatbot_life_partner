class UserMemory:
    def __init__(self):
        self.data = {}
        self.last_question = None


# Simple in-memory session store
SESSION_STORE = {}

def get_memory(session_id: str) -> UserMemory:
    if session_id not in SESSION_STORE:
        SESSION_STORE[session_id] = UserMemory()
    return SESSION_STORE[session_id]
