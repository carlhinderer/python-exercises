
class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackEmptyError(Exception):
    pass


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        if self.is_empty():
            raise StackEmptyError
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        new_top = StackNode(data)
        new_top.next = self.top
        self.top = new_top

    def peek(self):
        if self.is_empty():
            raise StackEmptyError
        return self.top.data
    
    def is_empty(self):
        return self.top is None