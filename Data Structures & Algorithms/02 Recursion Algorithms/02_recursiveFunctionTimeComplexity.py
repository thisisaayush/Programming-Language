'''
1. O(n) - Linear Time Complexity.
   - A linear time complexity recursive function performs a number of operations linearly proportional to the input size.
'''
def linear_time_recursion(n):
    if n == 0:
        return
    else:
        print(n)  # Operation
        linear_time_recursion(n - 1)

'''
2. O(log n) - Logarithmic Time Complexity.
   - A logarithmic time complexity recursive function reduces the problem size by a logarithmic factor with each 
     recursive call.
'''
def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)
