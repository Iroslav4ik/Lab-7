Задание №1
import requests

API_KEY = "ccdb69619380ff70770b62ee77682430"

city_name = "Prague"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=ru"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    city = data["name"]
    country = data["sys"]["country"]
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    weather_desc = data["weather"][0]["description"]

    print(f"Город: {city}, {country}")
    print(f"Температура: {temperature}°C (ощущается как {feels_like}°C)")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} hPa")
    print(f"Погода: {weather_desc.capitalize()}")

else:
    print("Ошибка! Проверьте API-ключ или название города.")

Задание №2
import requests
import json


api_key = 'e1a26a1aa24d45e78d18330094eea37c'

url = f"https://newsapi.org/v2/everything?q=apple&from=2025-03-03&to=2025-03-03&sortBy=popularity&apiKey={api_key}"

response = requests.get(url)

data = response.json()

if data['status'] == 'ok':
    for article in data['articles'][:5]:
        print("Заголовок:", article['title'])
        print("Автор:", article['author'])
        print("Источник:", article['source']['name'])
        print("Дата публикации:", article['publishedAt'])
        print("Описание:", article['description'])
        print("URL:", article['url'])
        print("-" * 50)
else:
    print("Ошибка при получении данных.")
