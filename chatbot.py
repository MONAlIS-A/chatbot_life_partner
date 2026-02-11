from rules import match_rule
from memory import UserMemory

class LifePartnerChatbot:
    def __init__(self):
        self.memory = UserMemory()
        self.running = True

    def respond(self, user_input):
        response, action = match_rule(user_input, self.memory)

        if action == "EXIT":
            self.running = False

        return response
