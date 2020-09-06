
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Append is O(n) with no tail
    def append(self, data):
        end = Node(data)
        if self.head is None:
            self.head = end
            return
        current = self.head
        while current and current.next:
            current = current.next
        current.next = end

    # Delete is O(n)
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
        else:
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next

    # Search is O(n)
    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False