class MinStack:
    def __init__(self):
        self._stack = [] 
        self._minStack = []

    def push(self, val):
        self._stack.append(val)
        val = min(val, self._minStack[-1] if self._minStack else val) # if condition to check if self._minStack is empty or not.
        self._minStack.append(val)
    
    def pop(self):
        self._stack.pop()
        self._minStack.pop()
    
    def top(self):
        return self._stack[-1]
    
    def getMin(self):
        return self._minStack[-1]     
        
    