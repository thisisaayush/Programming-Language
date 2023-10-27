'''
Binary Tree: A binary tree is a hierarchical data structure in which each node has, at most, two children referred to as
             the left child and the right child.

In a Binary Tree:

             a. Root Node: It is the topmost node in the tree, and it serves as the starting point for traversing the tree.
             b. Internal Nodes: These nodes have at least one child.
             c. Leaf Nodes: These nodes have no children, and they are at the bottom of the tree.
             d. Edges: These are the lines or connectors that link nodes in the tree.

Binary trees are widely used in computer science and are fundamental in data structures and algorithms. They have several
variations and applications, including:

             a. Binary Search Tree (BST): A binary tree where the values in the left subtree are less than or equal to the
                root, and the values in the right subtree are greater than the root. BSTs are commonly used for efficient
                searching, insertion, and deletion of elements.

             b. Binary Heap: A binary tree with a special property. It can be either a min-heap, where the parent node's
                value is less than or equal to the values of its children, or a max-heap, where the parent node's value is
                greater than or equal to the values of its children. Heaps are used for priority queues and heapsort.

Other terminologies used in Binary Tree:

a. Height: In Binary Tree, height represents the number of edges between the root node and the current node. That's why, height
        starts from 0. Example: Height 0. Maximum number of Nodes in a Binary Tree = 2^(h+1) - 1
b. Level: In Binary Tree, level represents the number of nodes from the root node to the current node. That is why level starts
       from 1. Example: Level 1.
c. Degree of a Node: Number of sub-node or children a node has.
d. Degree of a Tree: The maximum number of degree a node has.


Types of Binary Tree:

a. Proper Binary Tree: Each node has either 0 or 2 children. It is also known as "Strict Binary Tree"
b. Full Binary Tree: Every internal node has exactly 2 children and all leaf nodes are at the same level.
                     Number of Nodes in a Full Binary Tree = 2^(h+1) - 1.
c. Complete Binary Tree: Nodes at each level are numbered from left to right without any gap.

'''