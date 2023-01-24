import tkinter as tk
import requests
import os
from tkinter import Label, Text, Button
from dotenv import load_dotenv

# TODO: Stop user from "Crtl + Enter" for textbox
# TODO: Ability for user to select metric or imperial(env var?)
# TODO: Get weather icon and display on window
# TODO: Display text from json on window

bg_color = "#2e3440"

class App(tk.Tk):

  def __init__(self):
    super().__init__()

    self.title('Weather App')
    self.attributes('-type', 'dialog')
    self.geometry("500x500")
    self.configure(bg=bg_color)

    self.label = Label(self, text="Weather", bg=bg_color, fg="white", font="JetbrainsMono, 50")
    self.label.pack()

    self.text = Text(self, width=20, height=1, font="JetbrainsMono, 15")
    self.text.pack(padx=10, pady=10)

    self.button = Button(self, width=10, height=2, text="Submit", command=self.get_weather)
    self.button.pack()

    self.weather_label = Label(self)

  def get_weather(self):
        city_name = self.text.get("1.0", "end-1c")

        load_dotenv()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ.get('KEY')}&units=metric").json()

        self.condition = weather_data['weather'][0]['main']
        self.desc = weather_data['weather'][0]['description'].title()
        self.temp = weather_data['main']['temp']
        self.feels_like  = weather_data['main']['feels_like']
        self.temp_min = weather_data['main']['temp_min']
        self.temp_max = weather_data['main']['temp_max']

        self.weather_label.config(text=self.temp_min)
        self.weather_label.pack()
        

if __name__ == "__main__":
  app = App()
  app.mainloop()
