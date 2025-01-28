import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def display_weather(weather_data):
    if not weather_data:
        return
    
    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    temp = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    
    print(f"\nWeather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {description.capitalize()}\n")

def main():
    print("Weather App")
    api_key = input("Enter your OpenWeatherMap API key: ")
    
    while True:
        city = input("\nEnter city name (or 'q' to quit): ").strip()
        if city.lower() == 'q':
            break
        
        if not city:
            print("Please enter a valid city name.")
            continue
        
        weather_data = get_weather(api_key, city)
        
        if weather_data and weather_data.get("cod") == 200:
            display_weather(weather_data)
        else:
            print(f"Could not retrieve weather data for {city}")

if __name__ == "__main__":
    main()