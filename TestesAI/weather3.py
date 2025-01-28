import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def get_weather(city):
    api_key = "fe68cb9ff0e2aa587a4369f000ac38ac"  # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extract relevant data
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"].capitalize()
        city_name = weather_data["name"]
        country = weather_data["sys"]["country"]

        return f"Weather in {city_name}, {country}:\n{temperature}°C, {description}"

    except requests.exceptions.HTTPError as e:
        return "City not found. Please try again."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to display weather in the app
def show_weather():
    city = city_entry.get()
    if city:
        weather_info = get_weather(city)
        weather_label.config(text=weather_info)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")

# Set up the GUI
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")

# Input field for city
city_label = tk.Label(app, text="Enter City:", font=("Arial", 12))
city_label.pack(pady=10)

city_entry = tk.Entry(app, font=("Arial", 12), width=25)
city_entry.pack(pady=5)

# Button to fetch weather
fetch_button = tk.Button(app, text="Get Weather", font=("Arial", 12), command=show_weather)
fetch_button.pack(pady=10)

# Label to display weather info
weather_label = tk.Label(app, text="", font=("Arial", 12), wraplength=300, justify="center")
weather_label.pack(pady=20)

# Run the app
app.mainloop()