class Node():
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class BinaryTree():
    def __init__(self):
        self.root = None

    def is_empty(self):
        if self.root == None:
            return True
        return False

    def display(self):
        self.__display(self.root, 0)

    def __display(self, node, level):
        if node == None:
            return
        self.__display(node.rchild, level + 1)
        for i in range(level):
            print(" ", end = " ")
        print(node.data)
        self.__display(node.lchild, level + 1)


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
        if node == None:
            return 0
        return max(self.__max_depth(node.lchild), self.__max_depth(node.rchild)) + 1



def main():
    bt = BinaryTree()
    bt.root = Node('P')
    bt.root.rchild = Node('Q')
    bt.root.lchild = Node('R')
    bt.root.rchild.rchild = Node('S')
    bt.root.rchild.lchild = Node('T')
    bt.display()
    print("\nPreorder traversal:  ")
    bt.preorder_traversal()
    print("\n\nInorder traversal:   ")
    bt.inorder_traversal()
    print("\n\nPostorder traversal: ")
    bt.postorder_traversal()
    print("\n\nHeight: ", bt.max_depth())


if __name__=="__main__":
    main()