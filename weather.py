import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        print(response.url)
        data = response.json()
        print(data)
        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'your_api_key' with your OpenWeatherMap API key
    api_key = '04913d3529a596d1a9b6e6717ef409dc'
    
    city = input("Enter the city name: ")
    get_weather(api_key, city)
