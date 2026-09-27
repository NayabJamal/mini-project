from tkinter import *
import requests

window = Tk()
window.title("Weather App")
window.geometry("400x300")


heading = Label(window, text="Weather App", font=("Arial", 16))
heading.pack(pady=10)


city_label = Label(window, text="Enter City:")
city_label.pack()


city_entry = Entry(window, width=25, font=("Arial", 12))
city_entry.pack(pady=5)

def get_weather():
    city = city_entry.get()

    if city == "":
        result_label.config(text="Please enter a city.")
        return

    try:
        api_key = ""
        
        url = "https://api.weatherapi.com/v1/current.json"

        parameters = {
            "key": api_key,
            "q": city
        }

        response = requests.get(url, params=parameters)

        data = response.json()

        if "error" in data:
            result_label.config(text="City not found.")
            return

        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]

        result_label.config(
            text=f"Temperature: {temperature}°C\n"
                 f"Condition: {condition}\n"
                 f"Humidity: {humidity}%"
        )

    except requests.exceptions.RequestException:
        result_label.config(text="Internet/API connection error.")



weather_button = Button(window, text="Get Weather", command=get_weather)
weather_button.pack(pady=10)


result_label = Label(window, text="")
result_label.pack(pady=20)

window.mainloop()