import tkinter as tk
from tkinter import messagebox
import requests

#The app is still not functioning. I will look at it some other time. Feel free to assist
# Constants
API_KEY ="e96d1792ed98606cfeab55ba201284ea"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather():
    """Fetch weather data and display it in the GUI."""
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # For temperature in Celsius
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raises an error for bad status codes (e.g., 401, 404)
        data = response.json()
        
        # Extract weather information
        city = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # Display weather details
        result_text.set(
            f"Weather in {city}, {country}:\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {weather_desc.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    except requests.exceptions.RequestException as e:
        result_text.set(f"Error fetching weather data: {e}")
    except KeyError:
        result_text.set("City not found. Please check the city name.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# City entry
tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Search button
tk.Button(root, text="Get Weather", command=fetch_weather).pack(pady=10)

# Result label
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", wraplength=300, font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
root.mainloop()
