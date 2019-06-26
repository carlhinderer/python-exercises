# Question 10
# Level 2
#
# Question:
#   Write a program that accepts a sequence of whitespace separated words as input and prints the words 
#     after removing all duplicate words and sorting them alphanumerically.
#
#   Suppose the following input is supplied to the program:
#     hello world and practice makes perfect and hello world again
#   Then, the output should be:
#     again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

def print_unique_sorted_words():
    words = get_words()
    sorted_and_unique = sort_and_unique_words(words)
    print(' '.join(sorted_and_unique))

def get_words():
    words = input('Enter the list of words: ')
    return words.split(' ')

def sort_and_unique_words(words):
    words = list(set(words))
    words.sort()
    return words


if __name__ == '__main__':
    print_unique_sorted_words()