#
# 1.1 Is Unique
#
# Implement an algorithm to determine if a string has all unique characters. 
#   What if you cannot use additional data structures? 
#

def unique_(s):
    return unique_with_set(s)

# With set, we make one pass, keeping track of characters we've seen
def unique_with_set(s):
    seen = set()
    for c in s:
        if c in seen:
            return False
        else:
            seen.add(c)
    return True

# Without using a data structure, we have to store results on the stack
def unique_with_stack(s):
    if len(s) < 2:
        return True
    if s[0] in s[1:]:
        return False
    return unique_with_stack(s[1:])


if __name__ == '__main__':
    print(unique('abcd'))