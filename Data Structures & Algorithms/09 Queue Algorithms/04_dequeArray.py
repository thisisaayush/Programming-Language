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