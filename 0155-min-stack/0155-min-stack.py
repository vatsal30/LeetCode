class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("-inf")

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min
        return self.min
        
    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()