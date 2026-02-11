from chatbot import LifePartnerChatbot

def main():
    bot = LifePartnerChatbot()
    print("💍 Life Partner Chatbot (Rule-Based)")
    print("Type 'start' to begin or 'bye' to exit.\n")

    while bot.running:
        user_input = input("You: ")
        reply = bot.respond(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    main()
