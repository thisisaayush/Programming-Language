class Node:
    __slots__ = "_element", "_left", "_right"
    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self._root = None
    def insert(self, troot, e):
        temp = None
        while troot:
            temp = troot
            if e == troot._element:
                return

            elif e < troot._element:
                troot = troot._left

            elif e > troot._element:
                troot = troot._right


        n = Node(e, None, None)

        if self._root:
            if e < temp._element:
                temp._left = n

            elif e > temp._element:
                temp._right = n

        else:
            self._root = n

    def search(self, e):
        troot = self._root

        while troot:
            if e == troot._element:
                return True

            elif e < troot._element:
                troot = troot._left

            elif e > troot._element:
                troot = troot._right

        return False

    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end=" ")
            self.inorder(troot._right)


x = BinarySearchTree()
x.insert(x._root, 50)
x.insert(x._root, 80)
x.insert(x._root, 70)
x.insert(x._root, 35)
x.insert(x._root, 40)
print("Inorder Traversal: ")
x.inorder(x._root)
print("\nSearch the value: ")
print(x.search(70))