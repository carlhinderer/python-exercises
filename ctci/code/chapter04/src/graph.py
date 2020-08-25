
# Graph

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.visited = False


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_nodes(self, nodes):
        self.nodes.extend(nodes)


def depth_first_search(root):
    if root:
        print(root.data)
        root.visited = True
        for node in root.adjacent:
            if not node.visited:
                depth_first_search(node)


from collections import deque

def breadth_first_search(root):
    queue = deque()
    root.visited = True
    queue.append(root)
    
    while len(deque) > 0:
        node = queue.popleft()
        print(node.data)
        for adj_node in node.adjacent:
            if not adj_node.visited:
                adj_node.visited = True
                queue.append(adj_node)



# Test Data

# Adjacency List

# n0 = GraphNode('0')
# n1 = GraphNode('1')
# n2 = GraphNode('2')
# n3 = GraphNode('3')
# n4 = GraphNode('4')
# n5 = GraphNode('5')
# n6 = GraphNode('6')

# n0.set_adjacent([n1])
# n1.set_adjacent([n2])
# n2.set_adjacent([n0, n3])
# n3.set_adjacent([n2])
# n4.set_adjacent([n6])
# n5.set_adjacent([n4])
# n6.set_adjacent([n5])

# g = Graph()
# g.add_nodes([n0, n1, n2, n3, n4, n5, n6])