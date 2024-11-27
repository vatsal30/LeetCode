class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        if len(self.items) == 0:
            self.items.append((val, val))
            return
        min_val = self.getMin()
        if val < min_val:
            min_val = val
        self.items.append((val, min_val))

    def pop(self) -> None:
        if len(self.items) == 0:
            return None
        item = self.items[-1][0]
        del self.items[-1]
        return item

    def top(self) -> int:
        return self.items[-1][0]
        

    def getMin(self) -> int:
        return self.items[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()