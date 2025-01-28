import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x500")
        
        # Replace with your API key from OpenWeatherMap
        self.api_key = "api key"
        
        # Create GUI elements
        self.setup_gui()
        
    def setup_gui(self):
        # City input
        self.city_label = tk.Label(self.root, text="Enter City:", font=('Arial', 14))
        self.city_label.pack(pady=10)
        
        self.city_entry = tk.Entry(self.root, font=('Arial', 12))
        self.city_entry.pack(pady=5)
        
        # Search button
        self.search_button = tk.Button(
            self.root,
            text="Get Weather",
            command=self.get_weather,
            font=('Arial', 12)
        )
        self.search_button.pack(pady=10)
        
        # Weather info display
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.temp_label = tk.Label(self.info_frame, text="", font=('Arial', 20))
        self.temp_label.pack()
        
        self.desc_label = tk.Label(self.info_frame, text="", font=('Arial', 14))
        self.desc_label.pack()
        
        self.humidity_label = tk.Label(self.info_frame, text="", font=('Arial', 12))
        self.humidity_label.pack()
        
        self.wind_label = tk.Label(self.info_frame, text="", font=('Arial', 12))
        self.wind_label.pack()
        
        self.time_label = tk.Label(self.info_frame, text="", font=('Arial', 10))
        self.time_label.pack()
    
    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Error", "Please enter a city name")
            return
            
        try:
            # Make API request
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                # Extract weather information
                temp = data['main']['temp']
                desc = data['weather'][0]['description']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                
                # Update GUI labels
                self.temp_label.config(text=f"{temp:.1f}°C")
                self.desc_label.config(text=desc.capitalize())
                self.humidity_label.config(text=f"Humidity: {humidity}%")
                self.wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
                self.time_label.config(text=f"Last Updated: {datetime.now().strftime('%H:%M:%S')}")
            else:
                messagebox.showerror("Error", f"Error: {data['message']}")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Error", "Failed to connect to weather service")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()  # Fixed: Changed from Root() to Tk()
    app = WeatherApp(root)
    root.mainloop()