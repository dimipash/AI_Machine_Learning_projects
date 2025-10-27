import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")
    print(f"The current time is {time}")

def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        print(results)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("The query is ambiguous. Please be more specific.")
        print("Disambiguation error:", e)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any information on that topic.")
        print("Page error: No page found.")

def process_command(command):
    if 'time' in command:
        get_time()
    elif 'wikipedia' in command:
        speak("What should I search on Wikipedia?")
        query = recognize_speech()
        if query:
            search_wikipedia(query)
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that command.")
        print("Unrecognized command.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)        
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand.")
        return None
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return None

def start_voice_assistant():
    speak("Hello! I am your voice assistant. How can I help you today?")
    while True:
        command = recognize_speech()
        if command:
            process_command(command)

start_voice_assistant()
    
