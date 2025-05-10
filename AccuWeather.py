import requests
from tkinter import *

def get_weather():
    city = city_entry.get()
    api = "919016478ddd35fdda97566c3e99bb9c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Temperature: {temperature}°C\n"
            f"Weather: {weather}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    else:
        result = "City not found or API error."

    output_label.config(text=result)

w = Tk()
photo = PhotoImage(file = "C:\\Users\\abdul\\Desktop\\Weather App\\cloudy.png")
w.iconphoto(False, photo)
w.title("AccuWeather")
w.geometry("300x400")

city_entry = Entry(w, width=25, font=("Arial", 20,))
city_entry.pack(pady=20)
city_entry.insert(0, "Enter Location")

get_weather_btn = Button(w, text="Check Weather", command=get_weather, font=("Arial", 20))
get_weather_btn.pack()

output_label = Label(w, text="", font=("Arial",20), justify=LEFT, wraplength=250)
output_label.pack(pady=20)
w.mainloop()