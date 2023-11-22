'''
Heap: A heap is a specialized tree-based data structure that satisfies the heap property. The heap property depends on whether
it's a max-heap or a min-heap:

Two Types of Heap:
    1. Max-Heap Property: In a max-heap, for every node i other than the root, the value of i is less than or equal to the
       value of its parent. Mathematically, if P is the parent node of C (child node), then the value at P is greater than or equal
       to the value at C. This ensures that the largest element is at the root.

    2. Min-Heap Property: In a min-heap, for every node i other than the root, the value of i is greater than or equal to the
       value of its parent. Mathematically, if P is the parent node of C, then the value at P is less than or equal to the value at C.
       This ensures that the smallest element is at the root.

    Heaps are typically implemented as arrays, and the relationship between elements is determined by their indices. The heap property is
    maintained during operations like insertions and deletions. This makes heaps efficient for tasks where you need quick access to either
    the minimum or maximum element, such as in priority queues or heap sort algorithms.

    Common Operations on a Heap:
    1. Heapify: Converting an array into a heap. This operation ensures that the heap property is satisfied.
    2. Insertion: Adding a new element to the heap. The element is added at the end of the heap, and then the heap property is restored by
       "bubbling up" or "sifting up" the element.
    3. Deletion: Removing the root element from the heap. After removal, the last element is moved to the root, and then the heap property is
       restored by "bubbling down" or "sifting down" the element.
Example:
Consider a min-heap:
          1
        /   \
       2     3
      / \   / \
     17  19 36  7
    / \
   25 100

'''