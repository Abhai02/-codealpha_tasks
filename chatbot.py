import random
import nltk
import requests
import wikipedia
from nltk.chat.util import Chat, reflections

def get_wikipedia_summary(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"There are multiple results for this query: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "I couldn't find an answer. Try rephrasing your question."
    except Exception:
        return "I'm having trouble fetching information right now. Try again later."

pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing fine! How about you?", "I'm great! Thanks for asking."]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot created to assist you.", "You can call me ChatBot!"]
    ],
    [
        r"(.*) your name?",
        ["I am ChatBot, your friendly assistant!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer basic questions, and fetch information from Wikipedia!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "See you later!"]
    ]
]

def chatbot():
    print("Hello! I'm ChatBot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input(">> ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Goodbye! Have a great day!")
            break
        
        response = chat.respond(user_input)
        if response:
            print(response)
        else:
            print(get_wikipedia_summary(user_input))

if __name__ == "__main__":
    nltk.download('punkt')  # Ensure required data is downloaded
    chatbot()
