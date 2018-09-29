# Exercise 1
#
#
# [PROJECT] 99 Bottles of Beer On the Wall Lyrics
#
# GOAL
#
# Create a program that prints out every line to the song "99 bottles of beer on the wall." This should be a pretty simple 
# program, so to make it a bit harder, here are some rules to follow.
#
# RULES
#
#     If you are going to use a list for all of the numbers, do not manually type them all in. Instead, use a built in function.
#
#     Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
#
#     Remember, when you reach 1 bottle left, the word "bottles" becomes singular.
#
#     Put a blank line between each verse of the song.

def print99bottles():
	for i in range(99, 0, -1): printverse(i)

def printverse(count):
	print('%s bottles of beer on the wall, %s %s of beer' % (count, count, formattedbottle(count)))
	print('Take one down, pass it around, %s %s of beer on the wall\n' % (count - 1, formattedbottle(count - 1)))

def formattedbottle(count):
	return 'bottle' if count == 1 else 'bottles'

print99bottles()