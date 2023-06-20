def insertionSort(A):
    n = len(A)

    for i in range (n):
        c_Value = A[i]
        position = i 

        while position > 0 and A[position - 1] > c_Value:
            A[position] = A[position - 1]
            position = position - 1
        
        A[position] = c_Value