#
# 1.6 String Compression
#
# Implement a method to perform basic string compression using the counts of 
#   repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. 
#   If the "compressed" string would not become smaller than the original string, 
#   your method should return the original string. You can assume the string has only 
#   uppercase and lowercase letters (a-z).
#

def compress(s):
    compressed = ''
    current_letter = ''
    current_count = 0
    for c in s:
        if c == current_letter:
            current_count += 1
        else:
            if current_letter:
                compressed = '{}{}{}'.format(compressed, current_letter, current_count)
                current_letter = ''
                current_count = 0
            current_letter = c
            current_count = 1
    if current_letter:
        compressed = '{}{}{}'.format(compressed, current_letter, current_count)
    return compressed


def smallest_string(s):
    compressed = compress(s)
    if len(compressed) < len(s):
        return compressed
    else:
        return s