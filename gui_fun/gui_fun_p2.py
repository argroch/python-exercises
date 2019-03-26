from Tkinter import *

# root = Tk()

# root = mainloop()

# window = Tk()
# window.title("GUI fun")
# label = Label(window, text = "Hello World!").pack()
# window.mainloop()


window = Tk()
window.title("GUI")

# creating 2 frames TOP and BOTTOM
# top_frame = Frame(window).pack()
# bottom_frame = Frame(window).pack(side = "bottom")

# # now, create some widgets in the top_frame and bottom_frame
# btn1 = Button(top_frame, text = "Button1", fg = "red").pack()# 'fg - foreground' is used to color the contents
# btn2 = Button(top_frame, text = "Button2", fg = "green").pack()# 'text' is used to write the text on the Button
# btn3 = Button(bottom_frame, text = "Button2", fg = "purple").pack(side = "left")# 'side' is used to align the widgets
# btn4 = Button(bottom_frame, text = "Button2", fg = "orange").pack(side = "left")

# window.mainloop()
def say_hi():
	Label(window, text = "Hi").pack()

Button(window, text = "Click Me!", command = say_hi).pack() # 'command' is executed when you click the button

window.mainloop()