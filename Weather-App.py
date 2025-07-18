import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

# Function that requests data from OpenWeather API
# If the request is successful we set the label and temp
# to the corresponding labels in the UI
def findLocationAndTemp():
    user_input = locationName.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"
    weather_data = requests.get(url)

    if weather_data.json()['cod'] == 200:

        locationLabel.config(text=f"{locationName.get()}")
        temp = int(weather_data.json()['main']['temp'] - 273)
        cityTemp.set(f"{temp}")
    
    else:
        print(weather_data.json()['cod'])
        locationLabel.config(text="Please Enter a Valid Location")
        cityTemp.set("")

# INIT GUI
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

# Settings Styles for buttons labels and entries
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 12))
style.configure("TEntry", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

# Label to display the name of the City Searched by the User
locationLabel = ttk.Label(main_frame, text="", font=("Segoe UI", 14, "bold"))
locationLabel.pack(pady=(0, 10))

# Create a Label that will hold the value of Temperature
cityTemp = tk.StringVar()
tempLabel = ttk.Label(main_frame, textvariable=cityTemp, font=("Segoe UI", 20, "bold"))
tempLabel.pack(pady=(0, 20))

# Set a string variable for the entry
# Later used to set the name of the Location Label
locationName = tk.StringVar()
locationEntry = ttk.Entry(main_frame, textvariable=locationName, width=30)
locationEntry.pack(pady=5)

# Declare a button that runs the
# findLocationaAndTempCommand
# Bind the Enter key to also run that command for convenience
searchBtn = ttk.Button(main_frame, text="Search", command=findLocationAndTemp)
searchBtn.pack(pady=10)
root.bind("<Return>", lambda e: searchBtn.invoke())

root.mainloop()
