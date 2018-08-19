class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "List Empty. No element to pop"
        self.size -= 1
        return self.stack.pop()

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def peak(self):
        if self.is_empty():
            return "List Empty. No peak"
        return self.stack[-1]

    def stack_size(self):
        return self.size

    def display(self):
        return self.stack
