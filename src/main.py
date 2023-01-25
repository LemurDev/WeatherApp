import tkinter as tk
import requests
import os
import io
from tkinter import Label, Text, Button
from dotenv import load_dotenv
from PIL import ImageTk, Image  
import urllib

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

    self.button = Button(self, width=10, height=2, text="Submit", command=self.get_weather, bg=bg_color, fg="white", font="JetbrainsMono, 10")
    self.button.pack(padx=10, pady=10)

    self.weather_label = Label(self)

    self.photo_label = Label(self)

  def get_weather(self):
        city_name = self.text.get("1.0", "end-1c")

        load_dotenv()

        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={os.environ.get('KEY')}&units={os.environ.get('UNITS')}").json()

        self.condition = weather_data['weather'][0]['main']
        self.desc = weather_data['weather'][0]['description'].title()
        self.temp = weather_data['main']['temp']
        self.feels_like  = weather_data['main']['feels_like']
        self.temp_min = weather_data['main']['temp_min']
        self.temp_max = weather_data['main']['temp_max']
        self.icon = weather_data['weather'][0]['icon']

        self.weather_label.config(text="Condition: "  + self.condition + "\n" + "Description: " + self.desc + "\n" + "Current Temperature: " + str(self.temp) + "\n" + "Temperature Feels Like: " + "\n" + str(self.feels_like) + "\n" + "Temperature Minimum: " + str(self.temp_min) + "\n" + "Temperature Maximum: " + str(self.temp_max), bg=bg_color, fg="white", font="JetbrainsMono 15")
        self.weather_label.pack()

        url = f"https://openweathermap.org/img/wn/{self.icon}@2x.png"
        self.raw_data = urllib.request.urlopen(url).read()
        self.im = Image.open(io.BytesIO(self.raw_data))
        self.image = ImageTk.PhotoImage(self.im)

        self.photo_label.config(image=self.image, bg=bg_color)
        self.photo_label.pack()
        

        

if __name__ == "__main__":
  app = App()
  app.mainloop()
