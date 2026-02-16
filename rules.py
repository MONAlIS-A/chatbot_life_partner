
import random

# ----------------- English Rules -----------------
import random

def match_rule_english(message, memory):
    msg = message.lower()

    # Greetings
    if msg in ["hi", "hello", "hey", "hiya"]:
        greetings = [
            "Hello! 🌸 I’m happy to connect with you. How are you feeling today?",
            "Hey there! 💫 I’m here to listen and chat. How’s your heart today?",
            "Hi! 🌟 I’m excited to start this conversation with you. How’s your day going?"
        ]
        return random.choice(greetings), None

    # Goodbye
    elif msg in ["bye", "exit", "see you", "goodbye"]:
        farewells = [
            "Goodbye for now! 🌼 Wishing you peace and happiness.",
            "See you soon! 💖 Take care of yourself.",
            "Bye! 👋 Remember, I’m always here when you want to talk."
        ]
        return random.choice(farewells), "EXIT"

    # Ask about love/partner
    elif "love" in msg or "partner" in msg or "relationship" in msg:
        prompts = [
            "That’s beautiful ❤️ Tell me more about what you’re looking for in a partner.",
            "I’d love to hear — what qualities matter most to you in a relationship?",
            "Everyone has unique preferences 🌹 Do you have any deal-breakers or must-haves?"
        ]
        return random.choice(prompts), None

    # Mood / small talk
    elif "how are you" in msg or "how's it going" in msg:
        replies = [
            "I’m feeling great chatting with you! 🌟 How about you?",
            "I’m here and ready to listen 💖 How’s your day treating you?",
            "I’m just a bot, but I’m glad to be here with you 😊 How are you feeling?"
        ]
        return random.choice(replies), None
    # suggestion
    elif any(word in msg for word in [
    "honest", "tall", "short", "kind", "loyal", "caring",
    "funny", "respectful", "ambitious", "calm", "smart",
    "creative", "romantic", "supportive", "understanding",
    "patient", "hardworking", "friendly", "confident", "generous"]):
        suggestions = [
            "Honesty is such a powerful quality 🌸. It builds trust and makes relationships stronger. Do you also value openness and communication along with honesty?",
            "Height can be a preference 😎, but what matters most is how someone makes you feel. Do you think personality traits like kindness or respect are equally important?",
            "That’s a nice preference 🌼. Physical traits are one part of attraction, but emotional qualities often last longer. Would you like your partner to balance appearance with loyalty or care?",
            "Kindness is beautiful 💖. A kind partner often makes life feel lighter and happier. Do you also imagine them being supportive in tough times?",
            "Loyalty is a wonderful trait 🌟. It creates stability in relationships. Do you think loyalty should go hand-in-hand with respect and love?",
            "Caring partners bring warmth 💫. They make everyday life feel special. Do you also hope for someone who balances care with understanding?",
            "A funny partner makes life joyful 😂. Do you think humor should be balanced with seriousness in important moments?",
            "Respect is the foundation of love 🌹. Do you believe respect should always come before romance?",
            "Ambition is inspiring 🚀. Would you like a partner who motivates you to grow together?",
            "Calmness brings peace 🌊. Do you imagine a partner who helps balance stress with serenity?",
            "Intelligence is attractive 📚. Do you prefer someone who shares knowledge or someone who learns with you?",
            "Creativity adds color to life 🎨. Would you enjoy a partner who brings new ideas and imagination into your journey?",
            "Romance makes relationships magical 💕. Do you think romance should be shown daily or in special moments?",
            "Supportive partners are priceless 🤝. Do you imagine someone who stands by you in every challenge?",
            "Understanding builds deep connection 🌼. Do you want a partner who listens with empathy?",
            "Patience is golden ⏳. Do you think patience is key to solving conflicts in relationships?",
            "Hardworking partners inspire stability 💪. Would you like someone who balances work with family time?",
            "Friendliness makes bonds stronger 🌟. Do you prefer a partner who is social or more private?",
            "Confidence is empowering 🔥. Do you imagine a partner who leads with confidence or shares decisions equally?",
            "Generosity shows a big heart 💖. Do you think generosity should be balanced with practicality?"
        ]
        return random.choice(suggestions), None

        
    elif msg in ["cool", "good", "fine", "okay", "alright", "well"]:
        replies = [
            "Sounds really good 🌸. Now tell me, what qualities do you feel are most important in a life partner?",
            "Glad to hear that 💫. Let’s go a little deeper — what kind of qualities would you love to see in your future partner?",
            "Awesome! 😎 Since you’re feeling good, let’s talk about love — what’s one quality you’d want your partner to always have?",
            "That’s nice to hear 🌼. Thinking about relationships, what traits do you believe make a strong life partner?",
            "Cool! 🌟 Now I’m curious — what’s the first quality that comes to mind when you imagine your ideal partner?"
        ]
        return random.choice(replies), None
    
    elif msg in ["urdu"]:
        return match_rule_urdu(message, memory)


    # Generic casual replies
    else:
        generic_replies = [
            f"That’s interesting! 🌸 '{message}'. Tell about your life Quality .",
            f"Hmm, '{message}' — I’d love to hear what that means to you 💫",
            f"I see! '{message}' sounds thoughtful. Would you like to share more?",
            f"Thanks for sharing! 🌼 '{message}' makes me curious — what’s on your mind?",
            f"Interesting point! ✨ '{message}' — could you explain a bit more?",
            f"Wow, '{message}' — that sounds meaningful. How does it make you feel?",
            f"'{message}' — I’d love to dive deeper into that with you 💖",
            f"That caught my attention! 🌟 '{message}' — tell me the story behind it.",
            f"'{message}' — sounds important. Would you like to expand on it?",
            f"Cool thought! 😎 '{message}' — what inspired you to say that?"
        ]
        return random.choice(generic_replies), None




# ----------------- Urdu Rules -----------------
def match_rule_urdu(message, memory):
    msg = message.lower()

    # Greetings
    if msg in ["ہیلو", "سلام", "ہائے"]:
        greetings = [
            "وعلیکم السلام! آج آپ کیسا محسوس کر رہے ہیں؟",
            "ہیلو! آپ کی دن کیسا گزر رہا ہے؟",
            "ہائے! آج کا دن کیسا ہے؟"
        ]
        return random.choice(greetings), None

    # Goodbye
    elif msg in ["الوداع", "بند", "خدا حافظ"]:
        farewells = [
            "خدا حافظ! خوش رہیں 🙂",
            "الوداع! امید ہے آپ کا دن شاندار گزرا 🌸",
            "بہت اچھا! پھر ملاقات ہوگی 👋"
        ]
        return random.choice(farewells), "EXIT"

    # Ask about love/partner
    elif "محبت" in msg or "پارٹنر" in msg or "رشتہ" in msg:
        prompts = [
            "مزید بتائیں کہ آپ اپنے شریکِ حیات میں کیا چاہتے ہیں ❤️",
            "آپ اپنے شریکِ حیات میں سب سے اہم خصوصیات کونسی چاہتے ہیں؟",
            "کیا کوئی خاص چیز ہے جو آپ چاہتے ہیں یا نہیں چاہتے؟"
        ]
        return random.choice(prompts), None

    # Mood / small talk
    elif "آپ کیسے ہیں" in msg or "کیسا ہے" in msg:
        replies = [
            "میں ٹھیک ہوں! آپ کیسے ہیں؟ 😊",
            "سب اچھا ہے! آپ کا دن کیسا گزر رہا ہے؟",
            "میں تو تیار ہوں بات کرنے کے لیے! آپ کیسا محسوس کر رہے ہیں؟"
        ]
        return random.choice(replies), None

    # Generic casual replies
    else:
        generic_replies = [
            f"آپ نے کہا: '{message}'. دلچسپ بات ہے!",
            f"سمجھ گیا! '{message}' نے مجھے سوچنے پر مجبور کر دیا 😎",
            f"واہ! '{message}' واقعی دلچسپ ہے۔"
        ]
        return random.choice(generic_replies), None
