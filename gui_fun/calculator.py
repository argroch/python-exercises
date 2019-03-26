from Tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("312x324")
window.resizable(0, 0)

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

equation = ""
input_text = StringVar()

input_frame = Frame(window, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
input_frame.pack(side = TOP)
input_field = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg = "#eee", bd = 0, justify = RIGHT)
input_field.grid(row = 0, column = 0)
input_field.pack(ipady = 10)

btns_frame = Frame(window, width = 312, height = 272.5)
btns_frame.pack()

clear = Button(btns_frame, text = "AC", fg = "black", width = 32, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: clear_all()).grid(row = 0, column = 0, columnspan = 4)

seven = Button(btns_frame, text = "7", fg = "black", command = lambda: btn_click(7)).grid(row = 1, column = 0)
eight = Button(btns_frame, text = "8", fg = "black", command = lambda: btn_click(8)).grid(row = 1, column = 1)
nine = Button(btns_frame, text = "9", fg = "black", command = lambda: btn_click(9)).grid(row = 1, column = 2)
divide = Button(btns_frame, text = "/", fg = "black", command = lambda: btn_click("/")).grid(row = 1, column = 3)

four = Button(btns_frame, text = "4", fg = "black", command = lambda: btn_click(4)).grid(row = 2, column = 0)
five = Button(btns_frame, text = "5", fg = "black", command = lambda: btn_click(5)).grid(row = 2, column = 1)
six = Button(btns_frame, text = "6", fg = "black", command = lambda: btn_click(6)).grid(row = 2, column = 2)
multiply = Button(btns_frame, text = "x", fg = "black", command = lambda: btn_click("*")).grid(row = 2, column = 3)

one = Button(btns_frame, text = "1", fg = "black", command = lambda: btn_click(1)).grid(row = 3, column = 0)
two = Button(btns_frame, text = "2", fg = "black", command = lambda: btn_click(2)).grid(row = 3, column = 1)
three = Button(btns_frame, text = "3", fg = "black", command = lambda: btn_click(3)).grid(row = 3, column = 2)
subtract = Button(btns_frame, text = "-", fg = "black", command = lambda: btn_click("-")).grid(row = 3, column = 3)


zero = Button(btns_frame, text = "0", fg = "black", command = lambda: btn_click(0)).grid(row = 4, column = 0)
point = Button(btns_frame, text = ".", fg = "black", command = lambda: btn_click(".")).grid(row = 4, column = 1)
add = Button(btns_frame, text = "+", fg = "black", command = lambda: btn_click("+")).grid(row = 4, column = 2)
equal = Button(btns_frame, text = "=", fg = "black", command = lambda: btn_equal()).grid(row = 4, column = 3)



window.mainloop()