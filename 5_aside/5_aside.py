'''
Created on 23 June 2022

@author: Craig

Take a list of players and create two football teams.
Used this a few years ago when my friends and i played football on the regular

'''

import random

def get_random_player(players):
    return players.pop(random.randrange(len(players)))

team_1 = []
team_2 = []
players = ["Craig", "Sean", "Chris", "Matt", "Rob", "Dazza", "Kev", "Shea", "Kev B", "Darren"]

for x in range(len(players) // 2):
   team_1.append(get_random_player(players))
   team_2.append(get_random_player(players))

print("Team One: %s" % team_1)
print("Team Two: %s" % team_2)