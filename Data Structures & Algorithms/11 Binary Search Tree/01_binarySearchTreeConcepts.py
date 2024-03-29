'''
Binary Search Tree: A Binary Search Tree (BST) is a hierarchical data structure that organizes data in a way that allows
                    for efficient insertion, deletion, and search operations. It is a type of binary tree where each node
                    has at most two children: a left child and a right child.

The key property of a Binary Search Tree is that for any given node:
    a.  All nodes in the left subtree have keys less than or equal to the node's key.
    b.  All nodes in the right subtree have keys greater than the node's key.
    c. This property ensures that elements in the BST are ordered and can be efficiently searched.

Key characteristics of a Binary Search Tree:
    - Each node has a key (or value).
    - Each node can have at most two children (left and right).
    - The left subtree contains nodes with keys less than the parent node's key.
    - The right subtree contains nodes with keys greater than the parent node's key.
    - Inorder traversal of the tree yields elements in sorted order.

Common operations on a Binary Search Tree:
    a. Insertion: Adding a new node with a given key to the tree while maintaining the BST property.
    b. Deletion: Removing a node with a given key from the tree while preserving the BST property.
    c. Search: Finding a node with a given key in the tree efficiently. This operation takes advantage of the BST's
       structure to perform searches in O(log n) time on average.
    d. Traversal: Visiting all nodes in a specific order, such as inorder, preorder, or postorder traversal.


Note:
    Here are some specific examples of applications that use binary search trees:
    a. Database indexes: Databases use binary search trees to index their data. This makes it possible to quickly search
       for data in the database.
    b. Search engines: Search engines use binary search trees to index the web. This makes it possible to quickly search
       for web pages that contain a particular keyword.
    c. File systems: File systems use binary search trees to store the directories and files on a computer. This makes it
       possible to quickly find and access files.
    d. Operating systems: Operating systems use binary search trees to manage processes and threads. This helps to ensure
       that processes and threads are scheduled and executed efficiently.
    e. Compilers: Compilers use binary search trees to represent the symbol tables for the programs they are compiling.
       This helps the compiler to quickly find and resolve symbols.

They offer fast search times but are sensitive to the order in which data is inserted. In the worst-case scenario (when
data is inserted in sorted or nearly sorted order), a BST may degenerate into a linked list, resulting in inefficient search
times. To address this, balanced binary search trees, such as AVL trees and Red-Black trees, are used to maintain a balance,
ensuring consistent O(log n) search and insertion times.
'''