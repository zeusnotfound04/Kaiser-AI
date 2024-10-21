import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Zeus')
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Zeus")
    else:
        speak("Good Evening Zeus")
    speak("Hello, I’m Kaiser. Welcome to my demo! As I'm currently in the testing phase, I will seek your confirmation before executing any tasks.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Zeus said: {query}\n")
    except Exception as e:
        print("Sorry, could you repeat that?")
        return "none"
    return query.lower()
