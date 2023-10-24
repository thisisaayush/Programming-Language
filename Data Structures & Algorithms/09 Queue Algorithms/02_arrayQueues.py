class QueuesArray:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def isEmpty(self):
        return len(self._data) == 0
    
    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return 
        
        else: 
            return self._data.pop(0)
        
    def first(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        return self._data[0]
