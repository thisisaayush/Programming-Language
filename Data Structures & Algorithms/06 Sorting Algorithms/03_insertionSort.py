'''
Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. For small lists, or
lists that are almost sorted, insertion sort can be efficient and straightforward.

'''
def insertionSort(A):
    n = len(A)

    for i in range (n):
        current_Value = A[i]
        position = i 

        while position > 0 and A[position - 1] > current_Value:
            A[position] = A[position - 1]
            position = position - 1
        
        A[position] = current_Value