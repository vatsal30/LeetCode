class Solution:
    def findFirst(self, low, high, nums, target):
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low
    
    def findLast(self, low, high, nums, target):
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low - 1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.findFirst(0, len(nums), nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        last = self.findLast(first, len(nums), nums, target)
        return [first, last]
