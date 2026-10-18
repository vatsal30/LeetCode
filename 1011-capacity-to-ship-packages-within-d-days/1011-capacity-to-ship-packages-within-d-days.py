class Solution:
    def countDays(self, weights, capacity):
        days = 1
        current = 0
        for weight in weights:
            if current + weight <= capacity:
                current += weight
            else:
                days += 1
                current = weight
        return days

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high - low) // 2
            if self.countDays(weights, mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low