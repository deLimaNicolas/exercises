class MinStack:

    def __init__(self):
        self.values = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.values.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.values.pop()
        self.minStack.pop()


    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
