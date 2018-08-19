#Implement a queue with two stacks

from queues.stack_structure import Stack

class stack2_q:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        self.s1.push(item)

    def dequeue(self):
        if not self.s2.size > 0:
            self.inverted_content()
        return self.s2.pop()

    def inverted_content(self):
        while self.s1.size > 0:
            self.s2.push(self.s1.pop())

    def display(self):
        return self.s1.display()

    def size_queue(self):
        return self.s1.size
