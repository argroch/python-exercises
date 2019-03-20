# just a place to try things out
dict = {"Francis":40, "Maria":49, "Lucy":33}

friend = raw_input("Who is your friend? ")

for key in dict:
    if friend == key:
        enemy = key

print enemy
