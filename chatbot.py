# memory.py

_sessions = {}

def get_memory(session_id: str):
    if session_id not in _sessions:
        _sessions[session_id] = {
            "language": None,
            "last_message": None
        }
    return _sessions[session_id]
