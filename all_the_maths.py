"""
Create a program that will take two numbers and then gives the user a choice of what kind of arthimetic they'd like done to the two numbers. Include at least: add, subtract, multiply and divide. This time you really gotta use methods!
"""
import os

def menu(x,y):
    print "Choose an operation:"
    print "-------------------"
    print "1. Addition"
    print "2. Subtraction"
    print "3. Multiplication"
    print "4. Division"

    choice = int(raw_input())

    if choice == 1:
        add(x,y)
    elif choice == 2:
        subtract(x,y)
    elif choice == 3:
        multiply(x,y)
    elif choice == 4:
        divide(x,y)
    else:
        print "Invalid input. Try again."
        menu(x,y)

def add(x,y):
    print "%d + %d = %d" % (x,y,x+y)
    go_again(x,y)

def subtract(x,y):
    if x > y:
        print "%d - %d = %d" % (x,y,x-y)
    else:
        print "%d - %d = %d" % (y,x,y-x)
    go_again(x,y)

def multiply(x,y):
    print "%d x %d = %d" % (x,y,x*y)
    go_again(x,y)

def divising(x,y):
    if x % y == 0:
        print "%d / %d = %d" % (x,y,x/y)
    else:
        print "%d / %d = %d, with a remainder of %d" % (x,y,x/y,x%y)

def divide(x,y):
    if x > y:
        divising(x,y)
    else:
        divising(y,x)
    go_again(x,y)

def go_again(x,y):
    choice = raw_input("Would you like to perform another operation? ")
    if choice.lower() == "y" or choice.lower() == "yes":
        os.system('clear')
        # os.system('cls') on windows
        print "Your numbers: %d, %d" % (x,y)
        menu(x,y)
    else:
        print "Okay. Have a pleasant rest of your day."

print "Let's have fun with numbers!"
num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("And another: "))

menu(num1,num2)
