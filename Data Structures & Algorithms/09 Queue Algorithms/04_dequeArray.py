'''
DeQue (Double-ended Queue): In DeQue, elements can be added and removed from both ends of an array or a list.

Common use of DeQue:
    a. Implementing Stacks and Queues: Deques can be used to implement both stacks and queues. Depending on how you use
       it, you can mimic the behavior of either data structure.
    b. Sliding Window Problems: Deques are used in solving sliding window problems where you need to maintain a dynamic
       window of elements in an array efficiently.
    c. Efficient Insertion and Removal: Deques allow for efficient insertion and removal of elements from both ends,
       which can be useful in various scenarios.
'''

class DEQueArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def addFirst(self, e):
        self._data.insert(0, e)

    def addLast(self, e):
        self._data.append(e)

    def removeFirst(self):
        if self.isEmpty():
            print("Queue is empty!")
            return 

        return self._data.pop(0)
    
    def removeLast(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        
        return self._data.pop()
    
    def first(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        
        return self._data[0]
    
    def last(self):
        if self.isEmpty():
            print("Queue is empty!")
            return 
        
        return self._data[-1]