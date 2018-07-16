#singly linked list can be traversed in only one direction
#functions which we are going to perform on a linked list in this program are:
#get_size(),find(data),add(data),remove(data)

class Node:
    def __init__(self,data,n=None):
        self.data = data
        self.next = n
    def set_data(self,data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next_node(self, n):
        self.next = n
    def get_next_node(self):
        return self.next

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
    def add(self,data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size +=1
    def remove(self, data):
        this_node = self.root
        prev_node = None
        while(this_node):
            if this_node.get_data == data:
                if prev_node:
                    prev_node.set_next_node(this_node.get_next_node())
                else:
                    self.root = this_node.get_next()
                self.size -=1
                return "\nRemoved"
            else:
                prev_node = this_node
                this_node.get_next_node()
            return "\nNot Removed: Not in list"
    def find(self,data):
        this_node = self.root
        while(this_node):
            if this_node.get_data() == data:
                return "\nFound"
            elif this_node.get_next_node() == None:
                return "\nNot Found"
            else:
                this_node = this_node.get_next_node()
    def print_list(self):
        node = self.root
        ll = []
        while(node):
            ll.append(node.get_data())
            node = node.get_next_node()
        print(ll)


def main():
    myList = LinkedList()
    myList.add(5)
    myList.add(9)
    myList.add(3)
    myList.add(8)
    myList.add(9)
    print("size=" + str(myList.get_size()))
    myList.remove(8)
    print("size=" + str(myList.get_size()))
    print("Remove 15", myList.remove(15))
    print("size=" + str(myList.get_size()))
    print("Find 25", myList.find(25))
    myList.print_list()

main()


