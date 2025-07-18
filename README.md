# Weather App Documentation

## Overview

This is a simple desktop weather application built using Python's `tkinter` GUI library. It fetches the current temperature of a city from the OpenWeatherMap API and displays it in the app window.

---

## Features

- User can enter a city name.
- On clicking "Search" or pressing Enter, the app fetches the current temperature for the city.
- Displays city name and temperature in Celsius.
- Handles invalid city names by showing an error message.

---

## Requirements

- Python 3.x
- Packages:
  - `requests`
  - `beautifulsoup4` (imported but not used currently)
  - `python-dotenv`
  - `tkinter` (usually comes with Python)

- An OpenWeatherMap API key stored in a `.env` file as `API_KEY`.

---

## How it works

1. The app loads environment variables from `.env` via `python-dotenv`.
2. User inputs a city name into the text field.
3. When "Search" is clicked or Enter pressed:
   - The app sends a GET request to OpenWeatherMap API for that city.
   - If the city is valid (`cod == 200` in the API response), the temperature is extracted and converted from Kelvin to Celsius.
   - The city name and temperature are displayed in the GUI.
   - If invalid, an error message is shown.

---

## Code Structure

### API Key Loading

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')
```

### Main Function

```python
def findLocationAndTemp():
    user_input = locationName.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
    weather_data = requests.get(url)

    if weather_data.json()['cod'] == 200:
        locationLabel.config(text=f"{locationName.get()}")
        temp = int(weather_data.json()['main']['temp'] - 273)
        cityTemp.set(f"{temp}")
    else:
        locationLabel.config(text="Please Enter a Valid Location")
        cityTemp.set("")
```

### GUI Setup

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

locationLabel = ttk.Label(main_frame, text="", font=("Segoe UI", 14, "bold"))
locationLabel.pack(pady=(0, 10))

cityTemp = tk.StringVar()
tempLabel = ttk.Label(main_frame, textvariable=cityTemp, font=("Segoe UI", 20, "bold"))
tempLabel.pack(pady=(0, 20))

locationName = tk.StringVar()
locationEntry = ttk.Entry(main_frame, textvariable=locationName, width=30)
locationEntry.pack(pady=5)

searchBtn = ttk.Button(main_frame, text="Search", command=findLocationAndTemp)
searchBtn.pack(pady=10)

root.bind("<Return>", lambda e: searchBtn.invoke())

root.mainloop()
```

---

## Usage

1. Clone the repo.
2. Create a `.env` file in the same folder with:

```
API_KEY=your_openweather_api_key_here
```

3. Install dependencies:

```bash
pip install requests python-dotenv beautifulsoup4
```

4. Run the script:

```bash
python Weather-App.py
```

5. Enter a city name and press "Search" or Enter to get the temperature.

---

## Notes

- Temperature conversion subtracts 273 to convert from Kelvin to Celsius (approximate).
- GUI uses `ttk` widgets for better styling.
- No advanced error handling or input validation beyond API response check.
