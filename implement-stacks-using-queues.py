class MyStack:

    def __init__(self):
        self.values = []
        
    def push(self, x: int) -> None:
        self.values.append(x)
        
    def pop(self) -> int:
        return self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def empty(self) -> bool:
        return self.values == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
