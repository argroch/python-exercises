from operator import itemgetter

class Team:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

teams = []

count = 0

team1 = Team("France",2)
teams.append(team1)
team2 = Team("Netherlands",4)
teams.append(team2)
team3 = Team("England",1)
teams.append(team3)
team4 = Team("Germany",3)
teams.append(team4)

# sorted(teams,key=itemgetter(x.rank))
teams.sort(key=lambda x: x.rank)

for team in teams:
    print "%d. %s" % (team.rank, team.name)
