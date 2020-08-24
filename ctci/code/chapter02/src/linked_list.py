
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append is O(n)
    def append(self, data):
        end = Node(data)
        if self.head is None:
            self.head = end
            return
        current = self.head
        while current and current.next:
            current = current.next
        current.next = end
