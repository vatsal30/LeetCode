from heapq import heappush, heappop
class NumberContainers:

    def __init__(self):
        self.num_loc = defaultdict(list)
        self.loc_num = {}
        
    def change(self, index: int, number: int) -> None:
        heappush(self.num_loc[number], index)
        self.loc_num[index] = number 
        

    def find(self, number: int) -> int:
        index = -1
        if number in self.num_loc:
            while len(self.num_loc[number]) > 0:
                num_idx = self.num_loc[number][0]
                if self.loc_num[num_idx] == number:
                    index = num_idx
                    break
                else:
                    heappop(self.num_loc[number])
        return index
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)