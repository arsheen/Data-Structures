#BST using recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, x):
        self.root = self.__insert(self.root, x)

    def __insert(self, node, val):
        if node is None:
            node = Node(val)
        elif val < node.data:
            node.lchild=self.__insert(node.lchild, val)
        elif val > node.data:
            node.rchild=self.__insert(node.rchild, val)
        else:
            print("Node already in tree")
        return node

    def search(self, val):
        return self.__search(self.root, val) is not None

    def __search(self, node, val):
        if node is None:
            return None
        elif node.data > val:
            return self.__search(node.lchild, val)
        elif node.data < val:
            return self.__search(node.rchild, val)
        return node

    def min_val(self):
        min = self.__min_val(self.root)
        return min.data

    def max_val(self):
        max = self.__max_val(self.root)
        return max.data

    def __min_val(self, node):
        if node.lchild is None:
            return node
        return self.__min_val(node.lchild)

    def __max_val(self, node):
        if node.rchild is None:
            return node
        return self.__max_val(node.rchild)

    def display(self):
        self.__display(self.root, 0)

    def __display(self, node, level):
        if node is None:
            return
        self.__display(node.rchild, level +1)
        for i in range(level):
            print(" ", end = " ")
        print(node.data)
        self.__display(node.lchild, level+1)

#Preorder traversal: Root node is traversed first
    def preorder_traversal(self):
        self.__preorder(self.root)

    def __preorder(self, node):
        if node == None:
            return
        print(node.data," ", end = " ")
        self.__preorder(node.lchild)
        self.__preorder(node.rchild)

#Inorder traversal: Root node is traversed in the middle.
    def inorder_traversal(self):
        self.__inorder(self.root)

    def __inorder(self, node):
        if node == None:
            return
        self.__inorder(node.lchild)
        print(node.data, " ", end=" ")
        self.__inorder(node.rchild)

#Post order traversal: Root node is traversed lasts
    def postorder_traversal(self):
        self.__postorder(self.root)

    def __postorder(self, node):
        if node == None:
            return
        self.__postorder(node.lchild)
        self.__postorder(node.rchild)
        print(node.data," ", end = " ")

    def max_depth(self):
        return self.__max_depth(self.root)

    def __max_depth(self, node):
        """

        :param node:
        :return:
        """
        if node == None:
            return 0
        return max(self.__max_depth(node.lchild), self.__max_depth(node.rchild)) + 1

    def delete(self, val):
        self.root = self.__delete(self.root, val)

    def __delete(self, p, x):
        if p is None:
            print("Tree does not exist")
            return
        if x <  p.data:
            p.lchild = self.__delete(p.lchild, x)
        elif x > p.data:
            p.rchild = self.__delete(p.rchild, x)
        else:
            if p.lchild is not None and p.rchild is not None:
                s = p.rchild
                while s.lchild:
                    s = s.lchild
                p.info = s.data
                p.rchild = self.__delete(p.rchild, s.data)
            else:
                if p.lchild is not None:
                    ch = p.lchild
                else:
                    ch = p.rchild
            p = ch
        return p





def main():
    bt = BinarySearchTree()
    bt.root = Node(20)
    bt.insert(25)
    bt.insert(70)
    bt.insert(2)
    bt.insert(7)
    bt.display()
    print("Min val:   ", bt.min_val())
    print("Max val:   ", bt.max_val())
    print("Preorder:  ", bt.preorder_traversal())
    print("Inorder:   ", bt.inorder_traversal())
    print("Postorder: ", bt.postorder_traversal())
    print("Height:    ", bt.max_depth(), "\n\n")
    bt.search(7)
    bt.delete(70)
    bt.display()



if __name__ == "__main__":
    main()
