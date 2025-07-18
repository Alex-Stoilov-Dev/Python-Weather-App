import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('API_KEY')

print(api_key)

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
