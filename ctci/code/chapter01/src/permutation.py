#
# 1.2 Check Permutation: 
#  
# Given two strings, write a method to decide if one is a permutation of the other.
#
from collections import Counter

def permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_counts, s2_counts = Counter(), Counter()
    for c in s1:
        s1_counts[c] += 1
    for c in s2:
        s2_counts[c] += 1
    for key in s1_counts:
        if not s1_counts[key] == s2_counts[key]:
            return False
    return True