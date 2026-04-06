from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.time[key]
        left = 0
        right = len(data) - 1
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            if data[mid][1] <= timestamp:
                ans = data[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return ans



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)