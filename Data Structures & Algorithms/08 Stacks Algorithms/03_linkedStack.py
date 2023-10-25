class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next
    
class StacksLinkedlist:
    
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0

    # addLast() function of linkedlist class.
    def push(self, e): # e is the value to be pushed.
        new_element = _Node(e, None)

        if self.isEmpty():
            self._top = new_element
        
        else: 
            new_element._next = self._top
            self._top = new_element

        self._size += 1

    def pop(self):

        if self.isEmpty():
            print("Stack is empty!")
            return
        
        e = self._top._element
        self._top = self._top._next
        self._size -= 1

        return e
    
    def top(self):

        if self.isEmpty():
            print("Stack is empty!")
            return
        
        return self._top._element
        

    def display(self):
        p = self._top

        while p:
            print(p._element, end=" ")
            p = p._next
        print()