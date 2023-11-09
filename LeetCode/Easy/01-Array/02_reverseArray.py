def revArray(arr):
    n = len(arr) - 1
    for i in range(len(arr) // 2):
        arr[i], arr[n - i] = arr[n - i], arr[i]

    return arr


print(revArray([1, 2, 3, 4, 5]))