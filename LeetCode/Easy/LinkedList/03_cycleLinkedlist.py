class Node:
    def __init__(self, element, next=None):
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

    def addLast(self, e):
        newNode = Node(e)

        if self.isEmpty():
            self._head = newNode

        else:
            self._tail._next = newNode

        self._tail = newNode
        self._size += 1

    def middleElement(self):
        if self.isEmpty():
            print("Empty Linkedlist.")
            return

        slowPointer = self._head
        fasterPointer = self._head

        while fasterPointer and fasterPointer._next:
            slowPointer = slowPointer._next
            fasterPointer = fasterPointer._next._next

        return slowPointer._element

    def hasCycle(self):
        if self.isEmpty():
            print("Empty Linkedlist.")
            return

        slowPointer = self._head
        visited = set()
        p = self._head

        while p:
            if slowPointer in visited:
                return True
            visited.add(p)
            p = p._next

        return False
