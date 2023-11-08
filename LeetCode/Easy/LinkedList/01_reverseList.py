class Node:
    __slots__ = '_element', '_next'
    def __init__(self, element, next=None):
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

    def addLast(self, e):
        newNode = Node(e)

        if self.isEmpty():
            self._head = newNode

        else:
            self._tail._next = newNode

        self._tail = newNode
        self._size += 1

    def reverse(self):
        current = self._head
        prev = None

        while current is not None:
            nextNode = current._next
            current._next = prev
            prev = current
            current = nextNode

        self._head = prev

    def display(self):
        p = self._head

        while p:
            print(p._element, end = " ")
            p = p._next

my_linked_list = LinkedList()
my_linked_list.addLast(1)
my_linked_list.addLast(2)
my_linked_list.addLast(3)
my_linked_list.addLast(4)

# Display the original linked list
print("Original Linkedlist:")
my_linked_list.display()

# Reverse the linked list
my_linked_list.reverse()
print("\nReversed Linkedlist:")
my_linked_list.display()