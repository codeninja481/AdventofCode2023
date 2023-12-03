"""--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface 
of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, 
but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be 
happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get 
many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. 
Each time you play this game, he will hide a secret number of cubes of each color in the bag, 
and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, 
grab a handful of random cubes, show them to you, and then put them back in the bag. He'll 
do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each 
game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated 
list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). 
The first set is 3 blue cubes and 4 red cubes; 
the second set is 1 red cube, 2 green cubes, and 6 blue cubes; 
the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained 
only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded 
with that configuration. However, game 3 would have been impossible because at one point the 
Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because 
the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have 
been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 
13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""
Games = open("Day_Two_Cube_Conundrum_Input.txt").read().split('\n')
#Games = open("Day_Two_Cube_Conundrum_Part_1_Test_Input.txt").read().split('\n')

def siftGame(game):
	gCnt = 1
	blueCnt = greenCnt = redCnt = 0
	blueMax = 14
	redMax = 12
	greenMax = 13
	gPass = 1
	#print("Grabs: " + game)
	grabs = game.split("; ")
	for g in grabs:
		#print("grab " + str(gCnt) + " : " + str(g))
		gCnt = gCnt + 1
		cubes = g.split(", ")
		for c in cubes:
			#print(str(c))
			if str(c)[str(c).index(' ')+1:] == "blue":
				#print("Blue: " + str(c)[0:str(c).index(' ')])
				blueCnt = blueCnt + int(str(c)[0:str(c).index(' ')])
			if str(c)[str(c).index(' ')+1:] == "red":
				#print("Red: " + str(c)[0:str(c).index(' ')])
				redCnt = redCnt + int(str(c)[0:str(c).index(' ')])
			if str(c)[str(c).index(' ')+1:] == "green":
				#print("Green: " + str(c)[0:str(c).index(' ')])
				greenCnt = greenCnt + int(str(c)[0:str(c).index(' ')])
			#print("Red: " + str(redCnt) + " Green: " + str(greenCnt) + " Blue: " + str(blueCnt))
			if (redCnt > redMax or greenCnt > greenMax or blueCnt > blueMax):
				gPass = 0
		redCnt = greenCnt = blueCnt = 0

	return gPass

GameIDsCount = 0
count = 0
spaceIDX = 0
colonIDX = 0
currIDX = 0

for g in Games:
	#print(str(g))
	spaceIDX = str(str(g).index(' '))
	colonIDX = str(str(g).index(':'))
	#print("Game number: " + str(g)[int(spaceIDX):int(colonIDX)])
	if siftGame(str(g)[int(colonIDX)+2:]) == 1:
		GameIDsCount = GameIDsCount + int(str(g)[int(spaceIDX):int(colonIDX)])

	count = count + 1


print("Game IDs are: " + str(GameIDsCount))
print("Game IDs answer is: 2727")