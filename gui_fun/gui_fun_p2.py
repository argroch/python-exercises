from Tkinter import *
import time

class App():
	global start = time.time()
  def __init__(self):
    self.root = Tk()
    self.root.geometry("100x100")
    self.label = Label(text="")
    self.label.pack()
    self.update_clock()
    self.root.mainloop()

  def update_clock(self):
    now = time.strftime("%H:%M:%S")
    self.label.configure(text=now)
    self.root.after(1000, self.update_clock)

app=App()