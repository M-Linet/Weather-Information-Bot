import requests

def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    return response.json()

api_key = "10383e98ccfda7760bfe17a6ebbfd8ad"

def main():
    city = "London"
    weather_data = get_weather_data(city, api_key)
    print(weather_data)

if __name__ == "__main__":
    main()