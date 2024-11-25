from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]),
    (r"what is your name?", ["I am a chatbot created using NLTK.", "You can call me ChatBot!"]),
    (r"how are you?", ["I'm just a program, so I don't have feelings, but thanks for asking!"]),
    (r"what can you do?", ["I can chat with you about simple topics.", "I can help you feel less lonely for a while!"]),
    (r"(.*) your (creator|developer)", ["I was created by a programmer!", "I am the result of someone's hard work."]),
    (r"quit|bye", ["Goodbye!", "It was nice chatting with you!"]),
    (r"(.*)", ["I'm not sure I understand that. Could you rephrase?"])
]

# Initialize the chatbot
def chatbot():
    print("ChatBot: Hello! I am your friendly chatbot. Type 'bye' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
