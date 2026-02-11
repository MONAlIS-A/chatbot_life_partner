import random

FRIENDLY_ACKS = [
    "I see 😊",
    "That makes sense.",
    "Interesting!",
    "Thanks for sharing 💛",
    "Got it 👍"
]

def match_rule(user_input, memory):
    text = user_input.lower().strip()

    # -------- EXIT --------
    if text in ["bye", "exit", "quit"]:
        return "It was really nice talking with you 😊 Take care 💍", "EXIT"

    # -------- SMALL TALK --------
    if text in ["how are you", "how are you doing"]:
        return "I'm doing well 😊 How are you feeling today?", None

    if text in ["fine", "good", "okay", "alhamdulillah"]:
        return "That's good to hear 🌸 We can continue whenever you're ready.", None

    # -------- COMPLIMENTS --------
    if any(word in text for word in ["good bot", "nice", "helpful", "great"]):
        return "Thank you 😊 That really means a lot to me.", None

    # -------- HESITATION --------
    if any(word in text for word in ["not sure", "don't know", "confused"]):
        return "That’s completely okay 😊 Take your time.", None

    # -------- GREETING --------
    if any(word in text for word in ["hi", "hello", "hey"]) and memory.last_question is None:
        return (
            "Hello 😊 I'm here to have a friendly conversation about your future life partner.\n"
            "Type 'start' whenever you feel ready.",
            None
        )

    # -------- START --------
    if text == "start":
        memory.last_question = "ASK_QUALITIES"
        return "Let’s begin 🌸 What qualities do you value most in a life partner?", None

    # -------- QUALITIES --------
    if memory.last_question == "ASK_QUALITIES":
        memory.data["qualities"] = user_input
        memory.last_question = "ASK_AGE"
        return f"{random.choice(FRIENDLY_ACKS)} What age range do you feel comfortable with?", None

    # -------- AGE --------
    if memory.last_question == "ASK_AGE":
        memory.data["age"] = user_input
        memory.last_question = "ASK_CAREER"
        return f"{random.choice(FRIENDLY_ACKS)} What kind of profession do you prefer?", None

    # -------- CAREER --------
    if memory.last_question == "ASK_CAREER":
        memory.data["career"] = user_input
        memory.last_question = "ASK_LOCATION"
        return f"{random.choice(FRIENDLY_ACKS)} Do you have any location or country preference?", None

    # -------- LOCATION --------
    if memory.last_question == "ASK_LOCATION":
        memory.data["location"] = user_input
        memory.last_question = "ASK_IMPORTANT_TOPIC"
        return (
            "That’s good to know 😊\n\n"
            "Apart from location, some things that really matter in a life partner are:\n"
            "• Values & morals\n"
            "• Religion or faith\n"
            "• Family mindset\n"
            "• Communication style\n"
            "• Lifestyle & future goals\n\n"
            "Which one feels most important to you right now?",
            None
        )

    # -------- IMPORTANT TOPIC --------
    if memory.last_question == "ASK_IMPORTANT_TOPIC":
        memory.data["important_topic"] = user_input
        memory.last_question = "ASK_IMPORTANT_DETAILS"
        return (
            f"That’s a very thoughtful choice 🌸\n"
            f"What matters most to you regarding {user_input}?",
            None
        )

    # -------- IMPORTANT DETAILS --------
    if memory.last_question == "ASK_IMPORTANT_DETAILS":
        memory.data["important_details"] = user_input
        memory.last_question = "SUMMARY"
        return generate_summary(memory), None

    return "I’m listening 😊 You can say 'start' to begin.", None


def generate_summary(memory):
    return f"""
💖 YOUR LIFE PARTNER VISION 💖

✨ Qualities         : {memory.data.get('qualities')}
✨ Age Range         : {memory.data.get('age')}
✨ Career Preference : {memory.data.get('career')}
✨ Location          : {memory.data.get('location')}
✨ Important Area    : {memory.data.get('important_topic')}
✨ Your Thoughts     : {memory.data.get('important_details')}

You have a very thoughtful mindset 🌸
If you want to explore more or refine anything, I’m here 😊
"""
