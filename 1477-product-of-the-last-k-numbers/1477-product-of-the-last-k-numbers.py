class ProductOfNumbers:

    def __init__(self):
        self.size_without_zero = 0
        self.prefixProd = [1]
        
    def add(self, num: int) -> None:
        if num == 0:
            self.prefixProd = [1]
            self.size_without_zero = 0
        else:
            self.prefixProd.append(self.prefixProd[-1] * num)
            self.size_without_zero += 1

    def getProduct(self, k: int) -> int:
        if k > self.size_without_zero:
            return 0
        else:
            return self.prefixProd[self.size_without_zero] // self.prefixProd[self.size_without_zero-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)