class Node:
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

    def find_middle(self):
        if self.isEmpty():
            print("Empty Linkedlist.")
            return None

        e = self._size // 2
        p = self._head
        i = 0

        while p:
            if i == e:
                return p._element
            else:
                p = p._next
                i += 1

    def display(self):
        current = self._head
        while current:
            print(current._element, end=" -> ")
            current = current._next
        print("None")

# Create a linked list
my_linked_list = LinkedList()
my_linked_list.addLast(1)
my_linked_list.addLast(2)
my_linked_list.addLast(9)
my_linked_list.addLast(4)
my_linked_list.addLast(5)
my_linked_list.addLast(5)

# Display the original linked list
print("Original Linked List:")
my_linked_list.display()

# Find the middle of the linked list
print("Middle Element: ", my_linked_list.find_middle())