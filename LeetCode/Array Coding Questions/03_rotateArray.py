#Rotate an Array to the right.
def rotateArray(array, k):
    k %= len(array)
    array[:] = array[-k] + array[:-k]