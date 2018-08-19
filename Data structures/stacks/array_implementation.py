class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def stack_size(self):
        return self.size

    def is_empty(self):
        if self.stack_size() == 0:
            return True
        return False

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("List is empty. No elements to pop")
            return
        print("Element popped: ", self.stack.pop())
        self.size -= 1

    def peak(self):
        if self.is_empty():
            print("List is empty. No elements at the peak")
            return
        print("Peak of stack: ", self.stack.pop())
        self.size -= 1

    def display(self):
        print("Stack: ", self.stack)


def main():
    s = Stack()
    s.push(5)
    s.push(17)
    s.push(25)
    s.push(50)
    s.display()
    s.pop()
    s.pop()
    s.peak()
    print("Size: ", s.stack_size())
    s.pop()
    s.pop()

if __name__ == "__main__":
    main()
