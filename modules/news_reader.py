import pyttsx3
from bs4 import BeautifulSoup
import requests

def read_news_aloud(news):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)

    if not news:
        print("No news available.")
        return

    for headline in news:
        print(headline)
        engine.say(headline)
        engine.runAndWait()

def get_latest_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = [headline.text.strip() for headline in soup.find_all('h2')]
        return headlines
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []
