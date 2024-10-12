import webbrowser
import requests

def search_on_browser(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)

def search_on_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)

def open_url_in_new_window(url):
    webbrowser.open_new(url)

def get_weather_report(api_key, city):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['current']['condition']['text']
        temperature = data['current']['temp_c']
        wind_speed = data['current']['wind_kph']
        humidity = data['current']['humidity']
        return weather_description, temperature, wind_speed, humidity
    return None, None, None, None

def generate_response(weather_description, temperature, wind_speed, humidity):
    if "sunny" in weather_description.lower():
        return f"It's sunny with {temperature}°C."
    # Add other weather conditions...
