import tkinter as tk
from tkinter import Label

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('My Awesome App')
    self.attributes('-type', 'dialog')
    self.geometry("500x500")
    self.configure(bg="blue")

    self.label = Label(self, text="Hello World!")
    self.label.pack()

if __name__ == "__main__":
  app = App()
  app.mainloop()
