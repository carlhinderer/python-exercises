# Exercise 3
#
#
# [PROJECT] Pythagorean Triples Checker
#
# BACKGROUND INFORMATION
#
# If you do not know how basic right triangles work, read this article on wikipedia.
#
# MAIN GOAL
#
# Create a program that allows the user to input the sides of any triangle, and then return whether the triangle is a Pythagorean 
#   Triple or not.
#
# SUBGOALS
#
#     If your program requires users to input the sides in a specific order, change the coding so the user can type in the sides 
#       in any order. Remember, the hypotenuse (c) is always the longest side.
#
#     Loop the program so the user can use it more than once without having to restart the program.

def triplechecker():
	a, b, c = promptforsides()
	triple = checkfortriple(a, b, c)
	printresult(triple)

def promptforsides():
	a = promptforside()
	b = promptforside()
	c = promptforside()
	return (a, b, c)

def promptforside():
	side = None
	while type(side) is not int:
		try:
			side = input('Enter the length of a side: ')
			side = int(side)
		except ValueError:
			print('The side lengths must be integers.')
	return side

def checkfortriple(a, b, c):
	if a > c: a, c = c, a
	if b > c: b, c = c, b
	return (a ** 2 + b ** 2 == c ** 2)

def printresult(triple):
	if triple:
		print("Yes, it's a Pythagorean Triple!")
	else:
		print("Nope, it's not a Pythagorean Triple.")

triplechecker()