class StockSpanner:

    def __init__(self):
        self.stack = []
        self.cnt = 1

    def next(self, price: int) -> int:
        prev_idx = self.cnt
        while self.stack and self.stack[-1][0] <= price:
            _, prev_idx = self.stack.pop()
        self.stack.append((price, prev_idx))
        self.cnt += 1
        return self.cnt - prev_idx

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)