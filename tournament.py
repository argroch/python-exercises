"""
Help match up teams for the first round in a seed-based tournament. In a seeded tournament, and during the first round, the top seed is matched with the bottom seed, the 2nd highest team is matched with the second lowest, etc.

Matchups:
(1) Wisconsin versus (4) Indiana,
(2) Michigan versus (3) Michigan State

If an odd number of teams are entered, the top-seeded team gets a bye (doesn't play)

Example:
Matchups:
(1) Wisconsin has a bye
(2) Michigan versus (5) Purdue
(3) Michigan State versus (4) Indiana
"""
import os
import time

teams = []

def clear_screen():
    # os.system('cls') # on windows
    os.system('clear')

def menu():
    clear_screen()
    print """Welcome to My Tournament Generator. Enter a selection:
    1. Enter teams
    2. List teams
    3. List matchups
    0. Exit program"""

    choice = int(raw_input())

    if choice == 1:
        enter_teams()
    elif choice == 2:
        list_teams()
    elif choice == 3:
        list_matchups()
    elif choice == 0:
        clear_screen()
        print "Goodbye for now!"
    else:
        clear_screen()
        print "Invalid choice. Try again!"
        time.sleep(1)
        menu()

# enter a team
def enter_teams():
    clear_screen()
    print "Enter a new team:"
    name = raw_input("What is the team name? ")
    rank = int(raw_input("Where are they on the ranking? "))

    team = Team(name, rank)
    teams.append(team)
    teams.sort(key=lambda x: x.rank)

    print """What next?
    1. Enter Another Team
    2. Back to Main Menu
    """

    choice = int(raw_input())
    if choice == 1:
        enter_teams()
    else:
        menu()

# list the teams
def list_teams():
    clear_screen()
    print "The teams are:"
    for team in teams:
        print "%d. %s" % (team.rank, team.name)
    ready = raw_input("When ready to go back to the menu, hit enter!")
    menu()

# list the matchups
def list_matchups():
    clear_screen()

    temp_teams = []
    for team in teams:
        temp_teams.append(team)

    print "Matchups:"

    if len(teams)%2 == 0:
        count = 0
        while count < len(temp_teams):
            print "(%d) %s versus (%d) %s" % (temp_teams[count].rank, temp_teams[count].name, temp_teams[-1].rank, temp_teams[-1].name)
            temp_teams.pop(-1)
            count += 1
    else:
        print "odd amount of teams"

    print ""
    ready = raw_input("When ready to go back to the menu, hit enter!")
    menu()

class Team:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

menu()
