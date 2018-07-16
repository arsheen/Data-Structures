#add two linked lists from left to right
link_list = []
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while(node != None):
            #print(node.val)
            link_list.append(node.val)
            node = node.next
        return link_list

    def add_r_l(l1,l2):
        #print("l1: ",l1,len(l1))
        #print("l2: ",l2,len(l2))

        len1 = len(l1) - 1
        #print(len1)
        len2 = len(l2) - 1
        oprd1 = 0
        oprd2 = 0

        for i in range(len(l1)):
            #print(i)
            oprd1 = l1[i] * ((10**len1) // (10**i)) + oprd1
            #print(("op1: ",oprd1))

        for j in range(len(l2)):
            oprd2 = l2[i] * ((10**len2) // (10**j)) + oprd2
            #print(("op2: ",oprd2))
        print(oprd1+oprd2)


if __name__ == "__main__":
    ll = [2, 2, 1, 1, 5]
    for i in ll:
        head = Node(i)
        a = head.traverse()
    print("a: ",a)

    x = a[:len(a)//2]
    y = a[len(a)//2:]

    print("x: ",x,"y: ",y)
    Node.add_r_l(x, y)

