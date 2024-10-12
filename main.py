from modules.voice_assistant import wishMe, takeCommand, speak
from modules.web_tasks import search_on_browser, search_on_youtube, open_url_in_new_window, get_weather_report, generate_response
from modules.music_player import play_random_song
from modules.news_reader import read_news_aloud
from config.urls import hanuman_chalisa, choliya_ke_huk_rajaji, tu_hai_kahan, central_cee_doja, rapper_banke_aa_gao_moda, brand_new

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("I got it Zeus. Ok I am Going to Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif "open youtube" in query:
            search_on_youtube("youtube.com")
            speak("Opening YouTube")

        elif "play music" in query:
            play_random_song()
            speak("Playing a random song from your playlist")

        elif "tell time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")

        elif "play hanuman chalisa" in query:
            open_url_in_new_window(hanuman_chalisa)

        # Add other conditions as required...
