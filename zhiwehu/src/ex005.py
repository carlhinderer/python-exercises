# Question 5
# Level 1
#
# Question:
# Define a class which has at least two methods:
#   getString: to get a string from console input
#   printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class StringHolder:
    def __init__(self):
    	self.string = ''

    def get_string(self):
    	self.string = input('Enter a string: ')

    def uppercase_string(self):
        return self.string.upper()

    def print_string(self):
    	print(self.uppercase_string())


if __name__ == '__main__':
	sh = StringHolder()
	sh.get_string()
	sh.print_string()