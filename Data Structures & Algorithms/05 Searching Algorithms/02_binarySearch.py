def binarySearch(A, n, key): # A is a sorted array, n is length of an array, and key is the value to be searched.
    left = 0
    right = len(A) - 1

    while left <=  right:
        mid = (left + right) // 2
        
        if A[mid] == key:
            return mid # return the key index.
        
        elif A[mid] > key:
            right = mid - 1
        
        elif A[mid] < key:
            left = mid + 1
    
    return "Key not found!"