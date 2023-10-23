'''
1. Search Algorithms
   - Search algorithms are a fundamental part of computer science and data processing. They are used to find a specific
     item (or items) in a collection of data, such as an array, list, or database. Various searching algorithms exist,
     each with its own characteristics, advantages, and use cases.

   - Below are explanations of some common searching algorithms:
      a. Linear Search: Time Complexity: O(n)
         - Linear search, also known as sequential search, is the simplest searching algorithm. It works by sequentially
           checking each element in the data structure until a match is found or the entire collection has been examined.
           If the element is found, it returns its position; otherwise, it returns a signal that the item is not present.

      b. Binary Search: Time Complexity: O(log n)
         - Binary search is used for searching in sorted arrays. It repeatedly divides the search interval in half,
           eliminating half of the remaining elements in each step. This algorithm is much faster than linear search but
           requires the data to be sorted.

      c. Hashing: Time Complexity: O(1) on average (with good hash function)
         - Hashing is a technique that uses a hash function to map data to a fixed-size array (hash table). The hash
           function calculates an index for each data element, making it very efficient for retrieving data. However,
           collisions (multiple data items hashing to the same index) need to be handled properly.

'''