'''
Selection sort algorithm finds the smallest element in the unsorted part of the array and swaps it with the element at
the current position during each iteration. This process continues until the entire array is sorted.
'''
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        # find the minimum element in the unsorted part.
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Sswap the found minimum element with the first element.
        arr[i], arr[min_index] = arr[min_index], arr[i]
