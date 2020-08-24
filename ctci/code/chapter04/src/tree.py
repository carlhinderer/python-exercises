
# Basic Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []


# Can wrap the Node class, but its rarely helpful or necessary
class Tree:
    def __init__(self):
        self.root = None



# Binary Tree

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def in_order_traversal(node):
    if node:
        in_order_traversal(node.left_child)
        print(node.data)
        in_order_traversal(node.right_child)

def pre_order_traversal(node):
    if node:
        print(node.data)
        pre_order_traversal(node.left_child)
        pre_order_traversal(node.right_child)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left_child)
        post_order_traversal(node.right_child)
        print(node.data)