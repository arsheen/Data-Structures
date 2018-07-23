#singly linked list can be traversed in only one direction
#functions which we are going to perform on a linked list in this program are:
#get_size(),find(data),add(data),remove(data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add_node(self, val):
        node = Node(val)
        self.root = node
        self.size += 1
        return node

    def remove_node(self, val):
        prev = None
        curr = self.root
        while (curr):
            if curr.data == val:
                if prev:
                    prev = curr.next
                else:
                     self.root = curr.next
            self.size -=1
            return True

            prev = curr
            curr = curr.next

    def get_size(self):
        return self.size

    def find(self,val):
        curr = self.root
        while(curr):
            if curr.data == val:
                return "Found"
            curr = curr.next
        return "Not Found"

    def print_list(self):
        node = self.root
        ll = []
        while(node):
            ll.append(node.data)
            node = node.next
        print(ll)

def main():
    myList = LinkedList()
    myList.add_node(15)
    myList.add_node(9)
    myList.add_node(3)
    myList.add_node(8)
    myList.add_node(25)
    print("size=" + str(myList.get_size()))
    print("Remove 8", myList.remove_node(8))
    print("size=" + str(myList.get_size()))
    print("Remove 15", myList.remove_node(15))
    print("size=" + str(myList.get_size()))
    print("Find 25", myList.find(25))
    myList.print_list()

main()













