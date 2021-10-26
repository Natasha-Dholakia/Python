#You need to calculate the points earned by a soccer team.
#The team won 18 games and ended 7 games as a draw.
#A win brings 3 points, while a draw brings 1.

#Easy Solution
#print = ((18 * 3) + (7 * 1))

print("How many games did the team win?")
wins = int(input())
print("How many games did the team draw?")
draws = int(input())
print("How many games did the team lose?")
losses = int(input())


points = (wins * 3) + (draws * 1)


print("The team has won", wins, "games, drawn", draws, "games and lost", losses, "games.")
print("The team has", points, "points.")

    
# The code below is used to test the code above.
# If you run this code, you should get the following output:
# How many games did the team win?
# 18
# How many games did the team draw?
# 7
# How many games did the team lose?
# 1
# The team has won 18 games, drawn 7 games and lost 1 games.
# The team has 27 points.





