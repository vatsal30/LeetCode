class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for num in set(nums):
            if num < k:
                return -1
            elif num > k:
                ans += 1
        return ans
            
        