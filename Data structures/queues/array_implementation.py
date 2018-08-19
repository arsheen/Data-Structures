class queues():

    def __init__(self, max):
        self.q = []
        self.size = 0
        self.max = max

    def queue(self, item):
        if self.max_length():
            return "Queue has reached its max length"
        self.q.append(item)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. No item to dequeue"
        self.size -= 1
        return self.q.pop(0)

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def display(self):
         return self.q

    def size_queue(self):
        return self.size

    def peak(self):
        return self.q[0]

    def max_length(self):
        if self.size == self.max:
            return True
        return False

if __name__ == "__main__":
    q = queues(5)
    q.queue(25)
    q.queue(30)
    q.queue(35)
    q.queue(55)
    print(q.display())
    q.dequeue()
    print(q.display())
    print(q.size_queue())


