import requests
import json

def get_weather(city, api_key):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(base_url)
    weather_data = response.json()
    return weather_data

def process_weather_data(weather_data):
    weather_description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    return weather_description, temperature, humidity

def main():
    api_key = "10383e98ccfda7760bfe17a6ebbfd8ad"  # Replace with your OpenWeatherMap API key
    city = input("Enter a city: ")
    weather_data = get_weather(city, api_key)
    weather_description, temperature, humidity = process_weather_data(weather_data)
    print(f"Weather in {city}: {weather_description}")
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")

if __name__ == "__main__":
    main()