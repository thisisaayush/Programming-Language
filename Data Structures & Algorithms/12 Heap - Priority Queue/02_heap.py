class Heap:
    def __init__(self):
        self._max = 10
        self._data = [0] * self._max
        self._csize = 0

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0

    def insert(self, e):
        if self._csize == self._max:
            print("Heap is full.")
            return

        self._csize += 1
        hi = self._csize

        while hi > 1 and e > self._data[hi // 2]:
            self._data[hi] = self._data[hi // 2]
            hi = hi // 2

        self._data[hi] = e

    def delete(self):
        if self._csize == 0:
            print("Heap is empty.")
            return

        e = self._data[1]
        self._data[1] = self._data[self._csize]
        self._csize = self._csize - 1

        i = 1
        j = i * 2

        while j <= self._csize:
            if self._data[j] < self._data[j + 1]:
                j = j + 1

            if self._data[i] < self._data[j]:
                temp = self._data[i]
                self._data[i] =self._data[j]
                self._data[j] = temp

                i = j
                j = i * 2

            else:
                break

            return e

    def maxHeap(self):
        if self.isEmpty():
            print("Heap is empty.")
            return

        return self._data[1]

heap = Heap()
heap.insert(25)
heap.insert(14)
heap.insert(2)
heap.insert(20)
heap.insert(10)
heap.insert(40)
print(heap._data)
print(heap.delete())
print(heap._data)