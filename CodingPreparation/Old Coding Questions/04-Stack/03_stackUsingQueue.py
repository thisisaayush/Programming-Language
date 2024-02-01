class StackUsingQueue:
    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def __len__(self):
        return  len(self._queue1)
