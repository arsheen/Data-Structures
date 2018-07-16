import p1

list_of_val = []
class Node(p1.Node):
    def k_to_last(self, k):
        node = self
        while(node != None):
            list_of_val.append(node.val)
            node = node.next

        if k in list_of_val:
            a = list_of_val.index(k)
            return list_of_val[a:]

        if not k in list_of_val:
            return "Not present in linked list"


if __name__ == "__main__":
    ll = [1, 5, 3, 7, 3, 2, 6]
    final = []
    for i in ll:
        head = Node(i)
        final = head.k_to_last(88)
    print(final)