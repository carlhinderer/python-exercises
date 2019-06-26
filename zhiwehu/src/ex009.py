# Question 9
# Level 2
#
# Question
#  Write a program that accepts sequence of lines as input and prints the lines after making all characters 
#    in the sentence capitalized.
#
#  Suppose the following input is supplied to the program:
#    Hello world
#    Practice makes perfect
#  Then, the output should be:
#    HELLO WORLD
#    PRACTICE MAKES PERFECT
#
# Hints:
#   In case of input data being supplied to the question, it should be assumed to be a console input.

def print_capitalized_lines():
    lines = get_lines()
    capitalized_lines = capitalize_lines(lines)
    for line in capitalized_lines:
        print(line)

def get_lines():
    lines = []
    while True:
        line = input('Enter a line, or enter "Done" if all lines have been entered: ')
        if line == 'Done': break
        lines.append(line)
    return lines

def capitalize_lines(lines):
    return [s.upper() for s in lines]


if __name__ == '__main__':
    print_capitalized_lines()