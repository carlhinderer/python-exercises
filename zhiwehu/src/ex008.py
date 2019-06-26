# Question 8
# Level 2
#
# Question:
#   Write a program that accepts a comma separated sequence of words as input and prints the words in a 
#     comma-separated sequence after sorting them alphabetically.
#
#   Suppose the following input is supplied to the program:
#     without,hello,bag,world
#   Then, the output should be:
#     bag,hello,without,world
#
# Hints:
#   In case of input data being supplied to the question, it should be assumed to be a console input.

def print_sorted_words():
    words = get_words()
    sorted_words = sort_words(words)
    print(','.join(sorted_words))

def get_words():
    word_list = input('Enter the words to be sorted: ')
    return word_list.split(',')

def sort_words(words):
    words.sort()
    return words


if __name__ == '__main__':
    print_sorted_words()