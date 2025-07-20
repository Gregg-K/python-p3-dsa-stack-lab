class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, value):
        if self.limit is not None and len(self.items) >= self.limit:
            raise OverflowError("Stack is full")
        self.items.append(value)

    def pop(self):
        if self.isEmpty():
            return None  # Changed from raising IndexError to returning None
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return self.limit is not None and len(self.items) >= self.limit

    def search(self, value):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == value:
                return len(self.items) - 1 - i
        return -1
