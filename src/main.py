import tkinter as tk

class App(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('My Awesome App')
    self.attributes('-type', 'dialog')
    self.geometry("500x500")
    self.configure(bg="blue")

if __name__ == "__main__":
  app = App()
  app.mainloop()
