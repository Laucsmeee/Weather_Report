import requests
import os
import datetime
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "Kyiv"
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=ua"

def get_weather():
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print("Помилка запиту:", data.get("message"))
        return None


    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    rain = data.get("rain", {}).get("1h",0)

    text = (

        f"Дата:{datetime.datetime.now()}\n"
        f"Температура в {CITY} {temp}\n"
        f"На вулиці {description}\n"
        f"Час дощу на сьогодні {rain}\n"
        f"-------------------------------\n"

    )

    return text

def save_to_file(text):
    with open("data/weather.txt", "a", encoding="utf-8") as file:
        file.write(text)
if __name__ == "__main__":
    weather_text = get_weather()
    if weather_text:
        save_to_file(weather_text)
        print("Погода записана")
