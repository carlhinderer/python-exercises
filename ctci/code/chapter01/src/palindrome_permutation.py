#
# 1.4 Palindrome Permutation: 
#  
# Given a string, write a function to check if it is a permutation of a palindrome.
#   A palindrome is a word or phrase that is the same forwards and backwards. A 
#   permutation is a rearrangement of letters. The palindrome does not need to be 
#   limited to just dictionary words. 
#
#   EXAMPLE Input: Tact Coa Output: True (permutations: "taco cat". "atco cta". etc.)   
#

from collections import Counter

def palindrome_permutation(s):
    no_whitespace = s.strip().replace(' ', '')
    counts = Counter(no_whitespace)
    odd_count = False
    for pair in counts.items():
        if pair[1] % 2 == 1:
            if odd_count:
                return False
            else:
                odd_count = True
    return True