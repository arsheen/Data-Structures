import p0

class Node(p0. Node):
    def traverse(self):
        node = self
        while(node != None):
            print(node.val)
            node = node.next

if __name__ == "__main__":
    ll=[1,7,3,7,3,2,6]
    for i in ll:
        head = Node(i)
        head.traverse()