class _Node:
    __slots__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = None
        
    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0
    
    def addFirst(self, e):
        newNode = _Node(e, None)
        
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
            
        else:
            newNode._next = self._head
            self._head = newNode
        
        self._size += 1
    
    def addLast(self, e):
        newNode = _Node(e, None)
        
        if self.isEmpty():
            self._head = newNode
            self._tail = newNode
        
        else:
            self._tail._next = newNode
        
        self._tail = newNode
        self._size += 1
    
    def addAny(self, e, position):
        newNode = _Node(e, None)
        i = 1 
        p = self._head
        
        while i < position - 1:
            p = p._next
            i += 1
            
        newNode._next = p._next
        p._next = newNode
        
        self._size += 1
            
    def removeFirst(self):
        if self.isEmpty():
            print("Empty List!")
            return
        
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        if self.isEmpty():
            self._tail = None
        
        return e

    def removeLast(self):
        if self.isEmpty():
            print("Empty List!")
            return 
        
        #it is single linkedlist, forward only. So, we use i.
        i = 1
        p = self._head
        
        while i < len(self) - 1:
            p = p._next
            i += 1
        
        self._tail = p
        e = p._next._element
        self._tail._next = None
        self._size -= 1
        
        if self.isEmpty():
            self._tail = None
        
        return e
    
    def removeAny(self, position):
        if self.isEmpty() or position < 1 or position > len(self):
            print("Empty List!")
            return
            
        i = 1
        p = self._head
        
        while i < position - 1:
            p = p._next
            i += 1
        
        e = p._next._element
        p._next = p._next._next
        self.size -= 1
        
        return e
    
    def search(self, target):
        p = self._head
        
        while p:
            if p._element == target:
                return True
            p = p._next
        return False
            
    def display(self):
        p = self._head
        
        while p:
            print(p._element , end="--")
            p = p._next