'''
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps
them if they are in the wrong order.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
