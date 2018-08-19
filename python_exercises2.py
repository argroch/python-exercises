import os

def next_exercise():
    ready = raw_input("When ready for the next exercise, hit enter!")
    # os.system('cls') on windows
    os.system('clear')


"""
Write a program that asks for a score (an integer), and assigns a letter grade based on the score.

Letter grades are assigned as follows:
100-90: A
 89-80: B
 79-70: C
 69-60: D
Less than 60: F
More than 100: "Wrong score"
"""
score = int(raw_input("What score did you get on the test? "))

if score > 100:
    print "That's not true. That's impossible!"
elif score >= 90:
    print "You got an A!"
elif score >= 80:
    print "You got a B!"
elif score >= 70:
    print "You got a C."
elif score >= 60:
    print "You got a D. Not great."
else:
    print "Oh, dang! You got an F!"


next_exercise()
"""
Create a program that takes two numbers from the user and find out if the first is divisible by the second. If not divisible, let user know what the remainder is.
"""
num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("And another, please: "))

if num1 > num2:
    x = num1
    y = num2
else:
    x = num2
    y = num1

if x > y:
    if num1 % num2 == 0:
        print "Divisible! %d / %d = %d" % (x,y,x/y)
    else:
        print "Not divisible! %d / %d = %d, with a remainder of %d" % (x,y,x/y, x%y)


next_exercise()
"""
Create a program that takes a name (or any word, really), and spells it out, one letter at a time (vertically). Then have the name/word spelled out in one line (horizontally), but with commas between each letter (but not after the last letter).
"""
word = raw_input("Give me a word: ")

x = 0
while x < len(word):
    print word[x].upper()
    x += 1

y = 0
while y < len(word):
    if y == (len(word) - 1):
        print word[y]
    else:
        print word[y] + ", ",
    y += 1


next_exercise()
"""
Write a program that translates one English word into Pig Latin. Because the rules for Pig Latin can vary, I'll be specific:

If the given word starts with a consonant, move only that consonant to end and then add "ay" to the end (e.g.: coffee -> offeecay, blogger -> loggerbay)
If the given word starts with a vowel, add "way" to the end of the word (e.g., office -> officeway).

Set conditions for if the word starts with more than one consonant (three being the most a word can start with).
"""
word = raw_input("Give me a word: ")

if word[0] in "bcdfghjklmnpqrstvwxyz":
    if word[1] in "bcdfghjklmnpqrstvwxyz":
        if word[2] in "bcdfghjklmnpqrstvwxyz":
            print word[3:] + word[0:3] + "ay"
        else:
            print word[2:] + word[0:2] + "ay"
    else:
        print word[1:] + word[0] + "ay"
else:
    print word + "way"


next_exercise()
"""
Create a Python program that finds how many prime numbers are between 1 and a number given by the user.
"""
# num = int(raw_input("Give me a number: "))
# amount = 1
# if num > 1:
#     for x in range(2, num+1):
#         for y in range(2, x):
#             if x % y == 0:
#                 break
#             else:
#                 amount += 1
# else:
#     print "Number must be higher than 1"
#
# print "There are %d prime numbers between 1 and %d" % (amount, num)


# next_exercise()
"""
Fizzbuzz: Write a program that prints the numbers from 1 to 100. But for multiples of three (3) print "Fizz" instead of the number, and for the multiples of five (5) print "Buzz". For multiples of both three (3) and five (5), print "FizzBuzz".
"""
x = 1

while x <= 100:
    if x % 3 == 0 and x % 5 == 0:
        print "FizzBuzz"
    elif x % 3 == 0:
        print "Fizz"
    elif x % 5 == 0:
        print "Buzz"
    else:
        print x
    x += 1


next_exercise()
"""
Create an array of test scores (anywhere from 0 to 100; sorry, no extra credit was given).
Then...
Print out the scores in ascending order.
Find the average of those test scores and print it out.
"""
from random import randint

scores = []

for x in range(10):
    scores.append(randint(1, 100))

print sorted(scores)

total = 0
for score in scores:
    total += score

print "The average score is: %d" % (total/len(scores))
