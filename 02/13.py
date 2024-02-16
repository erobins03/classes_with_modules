import urllib.request
import json
WEATHER_API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_APP_ID = "989160722ae88675e12e46b904eae12b"
WEATHER_UNITS = "imperial"
cities = ["seattle", "dogland", "chicago"]
def get_current_weather(city):
    weather_url = WEATHER_API_BASE_URL + "?q=" + city + "&units=" + WEATHER_UNITS + "&appid=" + WEATHER_APP_ID
    try:
        response = urllib.request.urlopen(weather_url)
        data = response.read()
        weather_data = json.loads(data)
        return weather_data["weather"][0]["description"]
    except urllib.error.HTTPError:
        return "no data for this " + city

for city in cities:
    print(get_current_weather(city))

