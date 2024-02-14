class _Node:
    __slots__ ='_element', '_left', '_right'
    
    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right
    
class BinaryTree:
    def __init__(self):
        self._root = None
    
    def makeTree(self, e, left, right):
        self._root = _Node(e, left._root, right._root)
        
    def inorder(self, troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element, end="--")
            self.inorder(troot._right)
            
    def preorder(self, troot):
        if troot:
            print(troot._element, end="--")
            self.preorder(troot._left)
            self.preorder(troot._right)
    
    def postorder(self, troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end="--")
            
            
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
a = BinaryTree()
x.makeTree(20, a, a)
y.makeTree(30, a, a)
z.makeTree(10, x, y)