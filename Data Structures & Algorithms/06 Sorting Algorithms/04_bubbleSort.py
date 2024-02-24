'''
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps
them if they are in the wrong order. In each outer loop, the largest unsorted element "bubbles up- out" to its correct 
position after swapping.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):# represents the number of elements still need to be compared.
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
