class RandomizedCollection:

    def __init__(self):
        self.elements = []
        self.mapping = defaultdict(set)

    def insert(self, val: int) -> bool:
        val_set = self.mapping[val]
        val_set.add(len(self.elements))
        self.elements.append(val)
        return len(val_set) == 1

    def remove(self, val: int) -> bool:
        if val in self.mapping:
            idx = self.mapping[val].pop()
            last_idx = len(self.elements) - 1
            self.elements[idx] = self.elements[last_idx]
            self.elements.pop()
            if len(self.mapping[val]) == 0:
                self.mapping.pop(val)
            if idx != last_idx:
                last_ele_set = self.mapping[self.elements[idx]]
                last_ele_set.remove(last_idx)
                last_ele_set.add(idx)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.elements)        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()