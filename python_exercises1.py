import os

def next_exercise():
    ready = raw_input("When ready for the next exercise, hit enter!")
    # os.system('cls') on windows
    os.system('clear')


"""
Write a program that asks for your favorite Crayola crayon and then takes the
string and yells it back in all caps and in reverse.
"""
crayon = raw_input("What is your favorite Crayola crayon? ")

print crayon.upper() + "!"
print crayon[::-1]


next_exercise()
"""
Write a program that asks for your mood for the day, then returns the length of the string. Then return the string with 'meow' prepended to it.
"""
mood = raw_input("How do you feel today? ")
print "That mood is %d letters long." % (len(mood))
print mood + "meow"


next_exercise()
"""
Write a program that takes two numbers from the user and shows the sum, difference, product and quotient of the two numbers.
"""
num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Okay, and another: "))

print "The sum of %d and %d is %d" % (num1, num2, num1+num2)
print "The difference between %d and %d is %d" % (num1, num2, abs(num1 - num2))
print "The product of %d and %d is %d" % (num1, num2, num1*num2)
if num1 > num2:
    print "The quotient of %d and %d is %d" % (num1, num2, num1/num2)
else:
    print "The quotient of %d and %d is %d" % (num2, num1, num2/num1)


next_exercise()
"""
Write a program that asks for a sentence. Then ask for their favorite word in that sentence. Then tell them what index that word starts at.
"""
sen = raw_input("Give me a sentence: ")
word = raw_input("Okay, now what is your favorite word in that sentence? ")

print "Hmm... looks like that word is at %d index" % (sen.find(" " + word) + 1)


next_exercise()
"""
Write a program that asks for the cost of your dinner at a restaurant. The program will return back to you a tip of 18% of your meal cost. Make sure the tip is always returned with two decimal places.
"""
cost = float(raw_input("How much does the bill come to? "))
tip = cost * 0.18
print "Okay, tip should be $%s" % str(("%.2f" % tip))


next_exercise()
"""
Write a program that accpets your age. Convert your age to how old you are in seconds. Convert your age to how old you would be on the 8 different planets (hint: search planet rotation conversion rates). Output what your age in years would be on each planet.
"""
age = raw_input("What is your age? ")
age_in_days = float(age) * 365

print "Whoa, you are %d seconds old!" % (age_in_days * 86400)
print "On Mercury, you'd be %s years old." % str("%.2f" % (age_in_days/87.97))
print "On Venus, you'd be %s years old." % str("%.2f" % (age_in_days/224.7))
print "On Mars, you'd be %s years old." % str("%.2f" % (float(age)/1.8808476))
print "On Juptier, you'd be %s years old." % str("%.2f" % (float(age)/11.862615))
print "On Saturn, you'd be %s years old." % str("%.2f" % (float(age)/29.447498))
print "On Neptune, you'd be %s years old." % str("%.2f" % (float(age)/84.016846))
print "On Uranus, you'd be %s years old." % str("%.2f" % (float(age)/164.79132))
print "On Pluto, you'd be %s years old. And, yes, I still consider Pluto a planet." % str("%.2f" % (float(age)/247.92065))


next_exercise()
"""
Create a Mad Libs program with at least 10 inputs and minimum of one each of these: verb, plural noun, adjective, preposition, geographical feature, object, number.
"""
import time

print "Let's play Mad Python Libs!"
time.sleep(2)
verb1 = raw_input("Give me a past-tense verb: ")
verb2 = raw_input("Give me another past-tense verb: ")
verb3 = raw_input("And another past-tense verb: ")
verb4 = raw_input("Okay, one more past-tense verb, please: ")
body_part = raw_input("Give me a body part: ")
name1 = raw_input("Give me a person's name: ")
name2 = raw_input("Give me another person's name: ")
plural_noun = raw_input("Give me a plural noun: ")
exclamation1 = raw_input("Give me an exclamation: ")
exclamation2 = raw_input("Give me another exclamation: ")
adverb = raw_input("Give me an adverb: ")
feeling = raw_input("Give me an feeling: ")
thing = raw_input("Give me noun/thing: ")

print "Okay, here's our story:"
time.sleep(4)
print "%s %s near a whole bunch of %s. He couldn't believe his %s! '%s! Just what I was looking for,' he %s. 'These will help me %s.' But at the same time, %s %s the same thing and was also very %s. The two of them %s at each other and said, '%s! Get your hands off my %s!'" % (name1.capitalize(), verb1, plural_noun, body_part, exclamation1.capitalize(), verb2, adverb, name2, verb3, feeling, verb4, exclamation2.capitalize(), thing)
