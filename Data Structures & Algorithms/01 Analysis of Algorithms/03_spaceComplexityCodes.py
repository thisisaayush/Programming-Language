'''
1. Constant Space- O(1)
The function has O(1) space complexity because it uses a constant amount of extra space (only one variable) regardless of the input.
'''
def sum_of_two_numbers(a, b):
    result = a + b
    return result

'''
2. Linear Space- O(n)
The space complexity is O(n) because it creates an array of size n, and the space required scales linearly with the input.
'''
def create_array_of_n_elements(n):
    arr = [0] * n
    return arr

'''
3. Logarithmic Space- O(log n)
Recursive binary search is an example of O(log n) space complexity because it uses the call stack for recursion.
The space complexity is O(log n) due to the recursive calls, which take up space on the call stack.
'''
def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)


'''
4. Linarthimic Space- O(n log n)
Merge sort is an example of O(n log n) space complexity because it creates temporary arrays during the merge step.
The space complexity is O(n log n) due to the recursive calls and the temporary arrays used during the merge step.
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

'''
5. Exponential Space- O(n^2)
The space complexity is O(n^2) because it creates a matrix with n rows and n columns, resulting in n^2 elements.
'''
def create_2d_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        matrix.append(row)
    # Optionally, you can print the matrix to confirm the result
    for row in matrix:
        print(row)
    return matrix
