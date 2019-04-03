from Tkinter import *

window = Tk()
window.title("Geo Quiz")
window.geometry("400x150")
top = Frame(window, width = 400, height = 25)
bottom = Frame(window, width = 400, height = 25)
top.pack(side = 'top', fill = 'x')
bottom.pack(side = 'bottom', fill = 'x')

prompt = Label(top, text='Give me a state: ')
prompt.pack(side='left')

ans = StringVar() 
ans_entry = Entry(top, width=16, textvariable = ans)
ans_entry.pack(side='left')
ans_entry.focus()

def clear():
  list = top.pack_slaves()
  for l in list:
    l.destroy()

response = StringVar()
score_keep = StringVar()
score = 0
guesses = 0
def comp_response(event):
  global response
  global score_keep
  global score
  global guesses
  states = ['California','Oregon','Washington','Idaho','Alaska','Hawaii']
  guesses += 1
  if guesses < len(states):
  	if ans.get() in states:
  		score += 1
  		response.set("Correct!")
  		score_keep.set("Your score: %d" % (score))
  		ans_entry.delete(0, END)
  	else:
  		response.set("Wrong!")
  		ans_entry.delete(0, END)
  else:
  	clear()
  	if ans.get() in states:
  		score += 1
  	score_keep.set("You got %d / %d" % (score, len(states)))


ans_entry.bind('<Return>', comp_response)

response_label = Label(top, textvariable = response, width=18)
response_label.pack(side='left')

score_label = Label(bottom, textvariable = score_keep)
score_label.pack(side='left')

window.mainloop()