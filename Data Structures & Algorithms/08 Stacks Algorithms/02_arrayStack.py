class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isEmpty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
            return
        
        return self._data.pop()
    
    def top(self):
        if self.isEmpty():
            print("Stack is empty!")
            return
        
        return self._data[-1]
    
