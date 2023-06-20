def selectionSort(A):
    n = len(A)

    for i in range (n - 1):
        position = i
        
        for j in range (i+1, n):
            if A[j] < A[position]:
                position = j
        
        temp = A[i]
        A[i] = A[position]
        A[position] = temp
        