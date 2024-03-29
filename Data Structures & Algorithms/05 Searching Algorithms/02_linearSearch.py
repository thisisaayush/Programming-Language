def linearSearch_1(A, key): # A is an array and key is the value to be searched.
    index = 0

    while index < len(A):
        if A[index] == key:
            return index # returns the index value of the key found.
        
        index += 1

    return "Key not found!"

'''Or'''

def linearSearch_2(A, key):
    for i, value in enumerate(A):
        if value == key:
            return i

    return -1