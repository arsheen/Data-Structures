nlist=[]
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    def traverse_no_duplicate(self):
        node=self
        while(node!=None):
            if (node.val not in nlist):
                nlist.append(node.val)
                print("Next value in list:",node.val)
                #print("Memory location of value:",node)
            node=node.next


nodes=[1,2,2,3,4,5,8,4,5,8,33,45,78,23,77,95]
for i in nodes:
    value = Node(i)
    Node.traverse_no_duplicate(value)
