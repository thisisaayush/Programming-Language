def maxMin(arr, k):
    arr.sort()
    minUnfairness = float('inf')
    
    for i in range (len(arr) - k + 1):
        currentUnfairness = arr[i + k - 1] - arr[i]
        minUnfairness = min(currentUnfairness, minUnfairness)
    
    return minUnfairness