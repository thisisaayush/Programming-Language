from Heaps import Heap

def heapSort(array):
    H = Heap()
    n = len(array)

    for i in range(n):
        H.insert(array[i])

    k = n - 1

    for i in range(H._csize):
        array[k] = H.delete()
        k = k - 1


a = [20,23,21,39,32,40]
print("Original Array: ", a)
heapSort(a)
print("Heap Sort: ", a)