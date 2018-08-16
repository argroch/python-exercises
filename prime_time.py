num = int(raw_input("Give me a number: "))
amount = 1
if num > 1:
    for x in range(2, num+1):
        for y in range(2, x):
            if x % y == 0:
                break
            else:
                amount += 1
else:
    print "Number must be higher than 1"

print "There are " + str(amount) + " prime numbers between 2 and " + str(num)
