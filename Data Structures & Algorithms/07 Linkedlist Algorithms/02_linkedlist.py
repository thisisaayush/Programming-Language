class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next
    
class Linkedlist:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def addFirst(self, e): # e is the value to be added to end node.
        new_element = _Node(e, None)

        if self.isEmpty():
            self._head = new_element
            self._tail = new_element

        else:
            new_element._next = self._head
            self._head = new_element
        
        self._size += 1
    
    def addLast(self, e):
        new_element = _Node(e, None)

        if self.isEmpty():
            self._head = new_element
        
        else:
            self._tail._next = new_element
        
        self._tail = new_element
        self._size += 1

    def addAny(self, e, position):
        new_element = _Node(e, None)
        p = self._head
        i = 1 

        while i < position - 1:
            p = p._next
            i += 1

        new_element._next = p._next
        p._next = new_element
        self._size += 1

    def deleteFirst(self):
        if self.isEmpty():
            print('List is empty!')
            return

        e = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.isEmpty():
            self._tail = None

        return e
    
    def deleteLast(self):
        if self.isEmpty():
            print('List is empty!')
            return 
        
        p = self._head
        i = 1

        while i < len(self) - 1:
            p = p._next
            i += 1

        self._tail = p
        p = p._next
        e = p._element
        self._tail._next = None
        self._size -= 1

        return e

    def deleteAny(self, position):
        p = self._head
        i  = 1

        while i < position - 1:
            p = p._next
            i += 1
        
        e = p._next._element
        p._next = p._next._next
        self._size -= 1

        return e

    def search(self, key): # key is the element to be searched. 
        p = self._head
        index = 0

        while p:
            if p._element == key:
                return index # return the index where the key is located.
            
            p = p._next
            index += 1
        
        return "Key not found!"
    
    def display(self):
        p = self._head

        while p:
            print(p._element, end=" ")
            p = p._next
        print()

my_linked_list = Linkedlist()
my_linked_list.addLast(1)
my_linked_list.addLast(2)
my_linked_list.addLast(3)
my_linked_list.addLast(4)

# Display the original linked list
print("Original Linked List:")
my_linked_list.display()