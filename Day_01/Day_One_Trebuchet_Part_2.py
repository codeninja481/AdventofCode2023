"""--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out 
with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on 
each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these 
together produces 281.
"""

Calibration = open("Day_One_Trebuchet_Input.txt").read().split('\n')
#Calibration = open("Day_One_Trebuchet_Part_2_Test_Input.txt").read().split('\n')

firstNum = 0
lastNum = 0
ptr = 0
printedOut = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
calibrationValue = 0
foundFirst = 0
calibrationCount = 0

for c in Calibration:
	#print("calibration is: " + str(c))
	for i in c:
		#print("i is: " + str(i))
		if i in ['o', 't', 'f', 's', 'e', 'n']:
			#print("i is possibly the start of a number.")
			if i == 'o' and str(c)[ptr:ptr+3] == "one":
				#print("found one")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(1)
				else:
					lastNum = str(1)
			if i == 't' and str(c)[ptr:ptr+3] == "two": 
				#print("found two")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(2)
				else:
					lastNum = str(2)
			if i == 't' and str(c)[ptr:ptr+5] == "three":
				#print("found three")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(3)
				else:
					lastNum = str(3)
			if i == 'f' and str(c)[ptr:ptr+4] == "four": 
				#print("found four")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(4)
				else:
					lastNum = str(4)
			if i == 'f' and str(c)[ptr:ptr+4] == "five":
				#print("found five")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(5)
				else:
					lastNum = str(5)
			if i == 's' and str(c)[ptr:ptr+3] == "six":
				#print("found six")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(6)
				else:
					lastNum = str(6)
			if i == 's' and str(c)[ptr:ptr+5] == "seven":
				#print("found seven")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(7)
				else:
					lastNum = str(7)
			if i == 'e' and str(c)[ptr:ptr+5] == "eight":
				#print("found eight")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(8)
				else:
					lastNum = str(8)
			if i == 'n' and str(c)[ptr:ptr+4] == "nine":
				#print("found nine")
				if foundFirst != 1:
					foundFirst = 1
					firstNum = lastNum = str(9)
				else:
					lastNum = str(9)
		ptr = ptr + 1
		if i.isnumeric():
			#print("calibration value is: " + str(i))
			if foundFirst != 1:
				foundFirst = 1
				firstNum = lastNum = str(i)
			else:
				lastNum = str(i)
	foundFirst = 0
	ptr = 0
	calibrationValue = int(str(firstNum) + str(lastNum))
	#print("Full calibration: " + str(calibrationValue))
	calibrationCount = calibrationCount + calibrationValue

print("Calibration is: " + str(calibrationCount))
print("Calibration answer is: 54824")