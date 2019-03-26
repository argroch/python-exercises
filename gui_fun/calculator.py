from Tkinter import *
import math

window = Tk()
window.title("Calculator")
window.geometry("305x300")
window.resizable(0, 0)

# def last_two_lines(result):
# 	global equation
# 	input_text.set(result)
# 	equation = result

def btn_click(x):
  global equation
  equation = equation + str(x)
  input_text.set(equation)

def btn_equal():
  global equation
  result = str(eval(equation))
  input_text.set(result)
  equation = result

def clear_all():
  global equation
  equation = ""
  input_text.set("")

def square_root():
	global equation
	result = str(math.sqrt(int(equation)))
	input_text.set(result)
	equation = result

def factorial():
	global equation
	result = str(math.factorial(int(equation)))
	input_text.set(result)
	equation = result

def sine():
	global equation

def cosine():
	global equation

def tangent():
	global equation

equation = ""
input_text = StringVar()

input_space = Frame(window, width = 305, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_space.pack(side = TOP)
input_field = Entry(input_space, font = ('arial', 20, 'bold'), textvariable = input_text, width = 50, bg = "#D5D8DC", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btn_space = Frame(window, width = 305, height = 250)
btn_space.pack()

clear = Button(btn_space, text = "AC", fg = "black", command = lambda: clear_all()).grid(row = 0, column = 0)
sqrt = Button(btn_space, text = "sqrt", fg = "black", command = lambda: square_root()).grid(row = 0, column = 1)
exponent = Button(btn_space, text = "x^y", fg = "black", command = lambda: btn_click("**")).grid(row = 0, column = 2)

seven = Button(btn_space, text = "7", fg = "black", command = lambda: btn_click(7)).grid(row = 1, column = 0)
eight = Button(btn_space, text = "8", fg = "black", command = lambda: btn_click(8)).grid(row = 1, column = 1)
nine = Button(btn_space, text = "9", fg = "black", command = lambda: btn_click(9)).grid(row = 1, column = 2)
divide = Button(btn_space, text = "/", fg = "black", command = lambda: btn_click("/")).grid(row = 1, column = 3)

four = Button(btn_space, text = "4", fg = "black", command = lambda: btn_click(4)).grid(row = 2, column = 0)
five = Button(btn_space, text = "5", fg = "black", command = lambda: btn_click(5)).grid(row = 2, column = 1)
six = Button(btn_space, text = "6", fg = "black", command = lambda: btn_click(6)).grid(row = 2, column = 2)
multiply = Button(btn_space, text = "x", fg = "black", command = lambda: btn_click("*")).grid(row = 2, column = 3)

one = Button(btn_space, text = "1", fg = "black", command = lambda: btn_click(1)).grid(row = 3, column = 0)
two = Button(btn_space, text = "2", fg = "black", command = lambda: btn_click(2)).grid(row = 3, column = 1)
three = Button(btn_space, text = "3", fg = "black", command = lambda: btn_click(3)).grid(row = 3, column = 2)
subtract = Button(btn_space, text = "-", fg = "black", command = lambda: btn_click("-")).grid(row = 3, column = 3)


zero = Button(btn_space, text = "0", fg = "black", command = lambda: btn_click(0)).grid(row = 4, column = 0)
point = Button(btn_space, text = ".", fg = "black", command = lambda: btn_click(".")).grid(row = 4, column = 1)
add = Button(btn_space, text = "+", fg = "black", command = lambda: btn_click("+")).grid(row = 4, column = 2)
equal = Button(btn_space, text = "=", fg = "black", command = lambda: btn_equal()).grid(row = 4, column = 3)



window.mainloop()