'''
1. LinkedList- A linkedlist is a common data structure used in computer science to organize and store a collection of
               elements, often referred to as nodes.

             - Each node contains two main components:
                     a. Data: This is the value or information that the node stores. It can be any data type, such as an
                              integer, string, or even a more complex data structure.

                     b. Pointer (or Reference): This is a reference to the next node in the sequence. In a singly linked
                        list, each node points to the next node. In a doubly linked list, each node has two pointers, one
                        pointing to the next node and the other pointing to the previous node.

             - Linked lists have some important characteristics:
                     a. Dynamic Size: Linked lists can dynamically change in size, meaning nodes can be added or removed
                        as needed without requiring a fixed amount of memory.

                     b. Sequential Access: Elements in a linked list are sequentially connected. To access a specific
                        element, you typically start at the head (the first node) and follow the pointers until you reach
                        the desired node.

                     c. Memory Efficiency: Linked lists can be more memory-efficient than arrays for certain operations
                        because they don't require a contiguous block of memory. They can expand as needed, but they require
                        additional memory for the pointers.

2. There are several types of linked lists, including:
    a. Singly Linked List: In a singly linked list, each node points to the next node in the sequence. It's the simplest
       type of linked list.

    b. Doubly Linked List: In a doubly linked list, each node has two pointers, one pointing to the next node and the other
       pointing to the previous node. This allows for efficient traversal in both directions.

    c. Circular Linked List: A circular linked list is a variation of a singly or doubly linked list in which the last node
       points back to the first node, creating a closed loop.

Linked lists are commonly used to implement other data structures and algorithms, such as stacks, queues, and symbol tables.
They are also used when dynamic memory allocation is needed, as opposed to arrays that require a fixed amount of memory.

However, linked lists can be less memory-efficient than arrays:
    a. Due to the extra memory needed for the pointers.
    b. They are not as cache-friendly as arrays for random access.

The choice between using an array or a linkedlist depends on the specific requirements of the application.
'''