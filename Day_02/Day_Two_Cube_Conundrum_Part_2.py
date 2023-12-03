"""--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure 
why the water stopped; however, he can show you how to get to the water source to check it out 
for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the 
fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If 
any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, 
respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the 
power of these sets?
"""
Games = open("Day_Two_Cube_Conundrum_Input.txt").read().split('\n')
#Games = open("Day_Two_Cube_Conundrum_Part_1_Test_Input.txt").read().split('\n')

def siftGame(game):
	blueMin = greenMin = redMin = 0
	#print("Grabs: " + game)
	grabs = game.split("; ")
	for g in grabs:
		#print("grab " + str(gCnt) + " : " + str(g))
		cubes = g.split(", ")
		for c in cubes:
			#print(str(c))
			if str(c)[str(c).index(' ')+1:] == "blue":
				#print("Blue: " + str(c)[0:str(c).index(' ')])
				if int(str(c)[0:str(c).index(' ')]) > blueMin:
					blueMin = int(str(c)[0:str(c).index(' ')])
			if str(c)[str(c).index(' ')+1:] == "red":
				#print("Red: " + str(c)[0:str(c).index(' ')])
				if int(str(c)[0:str(c).index(' ')]) > redMin:
					redMin = int(str(c)[0:str(c).index(' ')])
			if str(c)[str(c).index(' ')+1:] == "green":
				#print("Green: " + str(c)[0:str(c).index(' ')])
				if int(str(c)[0:str(c).index(' ')]) > greenMin:
					greenMin = int(str(c)[0:str(c).index(' ')])

	print("Blue: " + str(blueMin) + " Red: " + str(redMin) + " Green: " + str(greenMin))
	return blueMin * redMin * greenMin

GameTotalPower = 0
GamePower = 0
spaceIDX = 0
colonIDX = 0
currIDX = 0

for g in Games:
	#print(str(g))
	spaceIDX = str(str(g).index(' '))
	colonIDX = str(str(g).index(':'))
	GamePower = siftGame(str(g)[int(colonIDX)+2:])
	print("Game " + str(str(g)[int(spaceIDX):int(colonIDX)]) + " GamePower: " + str(GamePower))
	GameTotalPower = GameTotalPower + GamePower


print("Game IDs are: " + str(GameTotalPower))
print("Game IDs answer is: 56580")