class RandomizedSet:

    def __init__(self):
        self.value = {}
        self.numbers = []

    def insert(self, val: int) -> bool:
        if val in self.value:
            return False
        self.value[val] = len(self.numbers)
        self.numbers.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.value:
            idx_to_remove = self.value[val]
            last_val = self.numbers[-1]
            self.value[last_val] = idx_to_remove
            self.numbers[idx_to_remove] = last_val
            self.numbers.pop()
            self.value.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()