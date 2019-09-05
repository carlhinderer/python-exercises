# Problem 3
# 
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and 
#   deserialize(s), which deserializes the string back into the tree.
#
# For example, given the following Node class
# 
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
# The following test should pass:
#
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


def serialize(root):
    return "Node('%s')" % root.val

def deserialize(s):
    print('Deserialize')


def test_single_node_serialize():
    node = Node('test')
    s = serialize(node)
    assert s == "Node('test')"

def test_serialize_deserialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    result = deserialize(serialize(node)).left.left.val
    assert result == 'left.left'

if __name__ == '__main__':
    test_single_node_serialize()