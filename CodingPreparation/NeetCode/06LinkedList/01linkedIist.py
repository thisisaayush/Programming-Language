class _Node:
    __slots__ = "_element", "_next"
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
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
    
    def addAnywhere(self, e, p):
        newNode = _Node(e, None)
        i = 0
        current = self._head
        
        while i < p - 1:
           current = current._next
           i += 1
        
        newNode._next = current._next
        current._next = newNode
        self._size += 1
        
    def deleteFirst(self):
        
        if self.isEmpty():
            print("List is Empty!")
            return
        
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        
        if self.isEmpty():
            self._tail = None
        
        return e
    
    def deleteLast(self):
        
        if self.isEmpty():
            print("List is Empty!")
            return
        
        p = self._head
        i = 0 
        
        while i < len(self) - 1:
            p = p._next 
            i += 1

        self._tail = p
        e = p._next._element
        self.tail._next = None
        self._size -=1
        
        return e
    
    def deleteAnyWhere(self, p):
        
        if self.isEmpty():
            print("List is Empty!")
            return
        
        current = self._head
        i = 0
        
        while i < p - 1:
            current = current._next
            i += 1
            
        e = current._next._element
        current._next = current._next._next
        self._size -= 1
        
        return e
            
    
    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index

            index += 1
            p = p._next
        
    def display(self):
        p = self._head
        
        while p:
            print(p._element, end = "--")
            p = p._next
        
        
        
L = LinkedList()
L.addFirst(7)
L.addFirst(9)
L.addFirst(4)
L.addFirst(1)
L.addLast(8)
L.addAnywhere(5,3)

print("Size: ", len(L))