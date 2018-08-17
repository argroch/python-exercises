"""
The Remainder Challenge!

In Python, 6 / 4 == 1.
But what if we want the remainder also?
Write a program that asks for two (2) Integers, divides the larger by the smaller and returns the result including the remainder.
If either of the numbers is not an Integer, then don't accept the number and ask again.
Do not accept zero (0) as a number.
"""
def get_number():
    num = raw_input("Give me a number: ")
    num = int(integer_check(num))
    num = zero_check(num)
    return num

def integer_check(num):
    if "." in num:
        print "No floats! Just integers!"
        num = get_number()
    return num

def zero_check(num):
    if num == 0:
        print "Zero is unaaceptable!"
        num = get_number()
    return num

def divising(x,y):
    if x % y == 0:
        print "Divisible! " + str(x) + " / " + str(y) + " = " + str(x/y)
    else:
        print "Not divisible. "+ str(x) + " / " + str(y) + " = " + str(x/y) + ", with a remainder of " + str(x%y)

num1 = get_number()
num2 = get_number()

if num1 > num2:
    divising(num1,num2)
else:
    divising(num2,num1)
