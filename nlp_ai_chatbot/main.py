import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline

nltk.download('punkt_tab')
nltk.download('stopwords')

def clean_text(text):
    text = text.lower()    
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

def simple_chatbot(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there!",
        "how are you": "I'm doing well, thank you.",
        "what is your name": "I'm a simple chatbot.",
        "bye": "Goodbye!",
        "default": "I'm sorry, I didn't understand that.",
        "thanks": "You're welcome!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return responses["default"]

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def ai_chatbot(user_input):
    response = chatbot(user_input, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

def chatbot_system():
    print("Welcome to the Chatbot System!")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        elif any(word in user_input.lower() for word in ["hello", "how are you", "what is your name", "bye", "thanks"]):
            response = simple_chatbot(user_input)
            print("Chatbot:", response)
        else:
            response = ai_chatbot(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot_system()
        
        





















# import nltk
# import re
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from transformers import pipeline

# nltk.download('punkt_tab')
# nltk.download('stopwords')

# chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# def ai_chatbot(user_input):
#     response = chatbot(user_input, max_length=50, num_return_sequences=1)
#     return response[0]['generated_text']

# print(ai_chatbot("Hello, how are you?"))

# def clean_text(text):
#     text = text.lower()    
#     text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
#     tokens = word_tokenize(text)
#     tokens = [word for word in tokens if word not in stopwords.words('english')]
#     return " ".join(tokens)

# # print(clean_text("Hello, World! This is a test.")) 

# def simple_chatbot(user_input):
#     user_input = user_input.lower()

#     responses = {
#         "hello": "Hi there!",
#         "how are you": "I'm doing well, thank you.",
#         "what is your name": "I'm a simple chatbot.",
#         "bye": "Goodbye!",
#         "default": "I'm sorry, I didn't understand that.",
#         "thanks": "You're welcome!"
#     }

#     for key in responses:
#         if key in user_input:
#             return responses[key]

#     return responses["default"]

# # print(simple_chatbot("Hello, chatbot"))