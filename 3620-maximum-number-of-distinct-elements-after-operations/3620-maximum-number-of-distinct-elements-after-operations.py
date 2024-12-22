from collections import defaultdict
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums_set = set()
        smallest_unused = float('-inf')

        for num in nums:
            adjusted = max(smallest_unused, num - k)
            
            if adjusted <= num + k:
                nums_set.add(adjusted)
                smallest_unused = adjusted + 1
        return len(nums_set)
        