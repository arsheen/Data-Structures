#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.

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

def parentheses(str1):

    stack = Stack()
    pairs = {'}': '{', ')': '(', ']': '['}
    
    if str1 == "":
    return True

    for i in str1:
        if i in ('{', '[', '('):
            stack.push(i)
        if i in ('}', ']', ')'):
            key = stack.peak()
            if pairs[i] == key:
                stack.pop()
            else:
                return False
    return True

def main():
    print(parentheses("{{{}}}"))
    print(parentheses("{([)]]"))
    print(parentheses("(){}[]"))
    print(parentheses("{}[()]"))
    print(parentheses("{}[(])"))


if __name__ == "__main__":
    main()
