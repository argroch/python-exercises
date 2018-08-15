import random

print "Let's play Rock, Paper, Scissors!"
user_play = (raw_input("One, two, three, shoot: ")).lower()
plays = ["rock","paper","scissors"]
prog_play = random.choice(plays)
print "I chose " + prog_play

if (prog_play == "rock" and user_play == "paper") or (prog_play == "paper" and user_play == "scissors") or (prog_play == "scissors" and user_play == "rock"):
    print "You win!"
elif (prog_play == "rock" and user_play == "scissors") or (prog_play == "paper" and user_play == "rock") or (prog_play == "scissors" and user_play == "paper"):
    print "I win!"
else:
    print "It's a tie!"
