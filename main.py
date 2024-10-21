from modules.voice_assistant import wishMe, takeCommand, speak
from modules.web_tasks import search_on_browser, search_on_youtube, open_url_in_new_window, get_weather_report, generate_response
from modules.music_player import play_random_song
from modules.news_reader import read_news_aloud
from config.urls import hanuman_chalisa, choliya_ke_huk_rajaji, tu_hai_kahan, central_cee_doja, rapper_banke_aa_gao_moda, brand_new
import datetime
import wikipedia
import pyautogui
from fuzzywuzzy import process  # Import fuzzywuzzy for fuzzy matching

# Define individual action functions

def search_wikipedia(query):
    query = query.replace("wikipedia", "").strip()
    speak("I got it Zeus. Ok, I am going to Wikipedia...")
    results = wikipedia.summary(query, sentences=2)
    speak(results)

def play_music():
    play_random_song()
    speak("Playing a random song from your playlist")

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Time is {strTime}")

def introduce_kaiser():
    speak("Hello Sir! I am Kaiser, Zeus's personal assistant. I am here to help you with your tasks. And ready contribute in the Hansraj Hackfest")

def shut_down_kaiser():
    speak("Yes Sir. Kaiser shutting down itself")
    exit()

def search_on_browser_command(query):
    search_term = query.replace("kaiser search", "").strip()
    speak(f"Searching {search_term}")
    search_on_browser(search_term)

def move_right():
    pyautogui.hotkey('winleft', 'right')
    speak("Yes sir!")

def move_left():
    pyautogui.hotkey('winleft', 'left')
    speak("Yes sir!")

def about_akash_sir(): 
    speak("Mr. Akash Nigam, a VMware and MS Cloud Certified Professional, brings a wealth of expertise to his role as an educator. A proud alumnus of Punjab University, Chandigarh, he combines his industry knowledge with a genuine passion for teaching, making complex concepts accessible and engaging for his students. As a dedicated mentor, he inspires and guides learners on their journey to success, fostering both technical skills and confidence.")


def about_tanuj_sir():
       speak("Mr. Tanuj Dwivedi, an exceptional English teacher at Mahatma Hansraj Modern School, inspires students with his profound knowledge and passion for literature. His engaging teaching style and unwavering support make learning enjoyable and impactful, fostering a love for the English language. A true mentor, he nurtures young minds, guiding them not just academically but also in their personal growth.")
def minimize_windows():
    pyautogui.hotkey('winleft', 'm')
    speak("Got it, sir!")

def maximize_windows():
    pyautogui.hotkey('winleft', 'M')
    speak("Got it, sir!")



def handle_sorry():
    speak("Not a problem Sir..!")

def who_created_kaiser():
    speak("Kaiser was developed by a great developer, genius, multi-tasker, editor, cyber expert Mr. Zeus Not Found!")


command_map = {
    "wikipedia": search_wikipedia,
    "play music": play_music,
    "tell time": tell_time,
    "introduce yourself": introduce_kaiser,
    "shut down yourself": shut_down_kaiser,
    "kaiser search": search_on_browser_command,
    "move it right side": move_right,
    "move it left side": move_left,
    "minimise everything": minimize_windows,
    "maximize everything": maximize_windows,
    "who created kaiser": who_created_kaiser,
    "kaiser how are you doing": lambda: speak("I am fine, sir! How about you?"),
    "i am also fine": lambda: speak("Great to hear that, sir!"),
    "great work kaiser": lambda: speak("Not a problem, Zeus"),
    "good kaiser": lambda: speak("Yes sirrr!"),
    "hello kaiser": lambda: speak("Yes Zeus, I am here. Is there any task for me?"),
    "your features": lambda: speak("I can do a lot of things, Zeus. Just give me a command and I will try to execute it."),
    "do you know akash sir": about_akash_sir,
    "do you know tanuj sir": about_tanuj_sir,
}

sorry_phrases = ["sorry", "kaisr sorry", "sorry kaiser"]

if __name__ == "__main__":
    wishMe()
    while True: # command lene ke liye baar baar infinite loop
        query = takeCommand().lower()

      
        if query in sorry_phrases:
            handle_sorry()

        else:
            # Matching Algorithm
            best_match = process.extractOne(query, command_map.keys()) # using keys method on dictionary to get all keys
            if best_match[1] > 70:  # matching score checking
                command = best_match[0] #pehla element 0 hoga (zero based indexing)
                speak(f"Did you mean '{command}'?")
                confirmation = takeCommand().lower()
                if "yes" in confirmation:
                   
                    if command in ["wikipedia", "kaiser search"]:
                        command_map[command](query)
                    else:
                        command_map[command]()  
                else:
                    speak("Okay, please repeat your command.")
            else:
                speak("I didn't catch that Zeus. Can you speak it again ?")
