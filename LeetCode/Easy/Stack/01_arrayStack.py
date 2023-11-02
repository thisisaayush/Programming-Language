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
            return "Empty Stack."

        return self._data.pop()

    def top(self):
        if self.isEmpty():
            return "Empty Stack."

        return self._data[-1]

s = ArrayStack()
print(s.pop())
s.push(1)
x = s.pop()
print(x)