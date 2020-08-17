# 
# 1.5 One Away
#
# There are three types of edits that can be performed on strings: insert 
#   a character, remove a character, or replace a character. Given two strings, 
#   write a function to check if they are one edit (or zero edits) away.
#
#   EXAMPLE pale, ple -> true 
#           pales. pale -> true 
#           pale. bale -> true 
#           pale. bake -> false 
#

def one_away(s1, s2):
    if s1 == s2:
        return True