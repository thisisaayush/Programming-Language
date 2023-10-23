'''
When given sorted array, Merge Sort performs better than Quick Sort. The reasons are:

1. Stability: Merge sort is a stable sorting algorithm, which means that the relative order of equal elements is maintained.
   In a sorted array, you may have many equal elements (e.g., duplicates), and merge sort ensures that their order remains
   unchanged. Quick sort is not inherently stable.

2. Predictable Performance: Merge sort has a consistent and predictable performance. Its time complexity is O(n log n) in
   all cases, regardless of the input data's initial order. Quick sort, on the other hand, can have a worst-case time complexity
   of O(n^2) in certain scenarios, although its average-case time complexity is also O(n log n).

3. No Need for Extra Space: Merge sort can be implemented without the need for additional space by carefully managing the merging
   process. Quick sort, however, typically requires O(log n) extra space for its recursive function calls.

4. Adaptive Behavior: In some situations, merge sort can exhibit adaptive behavior. If a significant portion of the input data is
   already sorted or nearly sorted, merge sort can take advantage of this and perform better. Quick sort is generally not as adaptive in nature.
'''