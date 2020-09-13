
class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueEmptyError(Exception):
    pass


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        node = QueueNode(data)
        if self.last:
            self.last.next = node
        self.last = node
        if not self.first:
            self.first = self.last

    def dequeue(self):
        if not self.first:
            raise QueueEmptyError
        data = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        return data

    def peek(self):
        if not self.first:
            raise QueueEmptyError
        return self.first.data

    def is_empty(self):
        return self.first is None