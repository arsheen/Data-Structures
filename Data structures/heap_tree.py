class Heap:
    def __init__(self, max_size):
        self.heap_array = [None]*max_size
        self.max_size = max_size
        self.size = 0
        self.heap_array[0] = 999999999

    def insert(self, val):
        self.size += 1
        self.heap_array[self.size] = val
        self.restore_up(self.size)

    def restore_up(self, index):
        k = self.heap_array[index]
        parent_index = index//2
        while self.heap_array[parent_index] < k:
            self.heap_array[index] = self.heap_array[parent_index]
            index = parent_index
            parent_index = index//2
        self.heap_array[index] = k

    def restore_down(self, index):
        k = self.heap_array[index]
        lchild = 2*index
        rchild = lchild+1
        while rchild <= self.size:
            if k >= self.heap_array[lchild] and k >= self.heap_array[rchild]:
                self.heap_array[index] = k
                return
            else:
                if self.heap_array[lchild] > self.heap_array[rchild]:
                    self.heap_array[index] = self.heap_array[lchild]
                    index = lchild
                else:
                    self.heap_array[index] = self.heap_array[rchild]
                    index = rchild

            lchild = 2 * index
            rchild = lchild + 1

        #if nodes are even in  no.
        if lchild == self.size and k < self.heap_array[lchild]:
            self.heap_array[index] = self.heap_array[lchild]
            index = lchild
        self.heap_array[index] = k



    def delete_root(self):
        max_val = self.heap_array[1]
        self.heap_array[1] = self.heap_array[self.size]
        self.size -= 1
        self.restore_down(1)
        return max_val


    def display(self):
        for i in range(1, self.size +1):
            print(" ", self.heap_array[i], end=" ")

def main():
    a = Heap(10)
    a.insert(25)
    a.insert(35)
    a.insert(12)
    a.insert(33)
    a.insert(50)
    a.display()
    print("\t\n", a.delete_root())
    a.display()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)


