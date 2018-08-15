import random

print "Let's play Rock, Paper, Scissors!"
user_play = (raw_input("One, two, three, shoot: ")).lower()
plays = ["rock","paper","scissors"]
#prog_play = random.choice(plays)
prog_play = raw_input("ai input: ")
print "I chose " + prog_play

if (prog_play == "rock" and user_play == "scissors") or (prog_play == "scissors" and user_play == "paper") or (prog_play == "paper" and user_play == "rock"):
    print "I win!"
elif (prog_play == "rock" and user_play == "paper") or (prog_play == "paper" and user_play == "scissors") or (prog_play == "scissors" and user_play == "rock"):
    print "You win!"
else:
    print "It's a tie!"
