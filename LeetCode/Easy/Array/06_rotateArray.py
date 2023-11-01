def rotateArray(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]

    return arr

print(rotateArray([1,2,7,4,5],2))