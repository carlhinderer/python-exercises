# Problem 5
#
# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#   For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
# Given this implementation of cons:
# 
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

# Implement car and cdr.


def car(pair):
    return pair(lambda p, q: p)

def cdr(pair):
    return pair(lambda p, q: q)

def test_car():
    result = car(cons(3, 4))
    assert result == 3

def test_cdr():
    result = cdr(cons(3, 4))
    assert result == 4

if __name__ == '__main__':
    test_car()
    test_cdr()