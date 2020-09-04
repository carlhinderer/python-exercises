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

import string

CHARSET = string.ascii_lowercase + string.ascii_uppercase + ' '

def one_away(s1, s2):
    if s1 == s2:
        return True
    for char in CHARSET:
        if (char + s1) == s2:
            return True
    for i, c in enumerate(s1):
        if s1.replace(c, '', 1) == s2:
            return True
        for char in CHARSET:
            with_char_replaced = s1.replace(c, char, 1)
            with_char_inserted = '{}{}{}'.format(s1[:i], char, s1[i:])
            print(with_char_replaced)
            print(with_char_inserted)
            if s2 in [with_char_replaced, with_char_inserted]:
                return True
    return False