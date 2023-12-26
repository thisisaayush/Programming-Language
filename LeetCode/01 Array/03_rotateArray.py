#Rotate an Array to the Right.
def rotateArray1(array, k):
    k %= len(array)
    array[:] = array[-k:] + array[:-k]
    
    
#Rotate an Array to the Left.
def rotateArray2(array, k):
    k %= len(array)
    array[:] = array[k:] + array[:k]

arr = [1, 2, 3, 4, 5]
rotateArray2(arr, 2)
print(arr)