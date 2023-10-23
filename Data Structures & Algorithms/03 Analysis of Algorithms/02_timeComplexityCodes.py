'''
1. Constant Time- O(1)
The time complexity is O(1) because accessing the first element of an array is a constant-time operation.
'''
def print_first_element(arr):
    print(arr[0])


'''
2. Linear Time- (O(n))
The time complexity is O(n) because it iterates through the array once, and the number of operations scales linearly with the array size.
'''
def linear_search(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

'''
3. Logarithmic Time- (O(log n))
Binary search has a time complexity of O(log n) because it halves the search space with each iteration.
'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

'''
4. Linearithmic Time- (O(n log n))
Merge sort has a time complexity of O(n log n) because it repeatedly divides and combines the array.
'''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Copy data to temp arrays left_half and right_half
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Check if any element was left
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

'''
5. Quadratic Time- (O(n^2))
Bubble sort has a time complexity of O(n^2) because it involves nested loops.
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
