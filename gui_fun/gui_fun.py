#!/usr/bin/env python3

from tkinter import *

# class Window(Frame):
# 	def __init__(self, master=None):
# 		Frame.__init__(self, master)
# 		self.master = master

# root = Tk()
# app = Window(root)
# root.mainloop()
window = tkinter.Tk()
window.title("GUI fun")
label = tkinter.Label(window, text = "Hello World!").pack()
window.mainloop()