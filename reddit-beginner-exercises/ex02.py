# Exercise 2
#
#
# [Project] Magic 8 Ball
#
# Goal
#
# I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up and it 
#   gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
#
#     Allow the user to enter their question
#
#     Display an in progress message( i.e. "thinking")
#
#     Create 20 responses, and show a random response
#
#     Allow the user to ask another question or quit

import time
import random

RESPONSES = ['Looks Good',
             'Looks Bad',
             'Unsure',
             'Nope',
             'Yep',
             'Maybe',
             'Definitely',
             'No Way!',
             'Depends...',
             'The Future Is Cloudy',
             'It Is Certain',
             'It Is Uncertain',
             'It Can Be',
             'It Cannot Be',
             'Ask Again Tomorrow',
             'Ask Again Next Week',
             'Ask Again Next Month',
             'Ask Again Next Year',
             'Ask Again In Ten Years',
             'Never Ask About That Again!']

def magic8ball():
	promptforquestion()
	displayprogressmessage()
	displayresponse()
	promptforanother()

def promptforquestion():
	input('What is your question?\n')

def displayprogressmessage():
	time.sleep(1)
	print('Thinking...')
	time.sleep(3)

def displayresponse():
	print(random.choice(RESPONSES))

def promptforanother():
	response = input("Enter 'y' to ask another question or press Enter to quit.\n")
	if response == 'y': magic8ball()

magic8ball()