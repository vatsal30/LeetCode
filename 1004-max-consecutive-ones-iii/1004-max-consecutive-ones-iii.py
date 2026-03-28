class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        noZero = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                noZero += 1
            while noZero > k:
                val = nums[left]
                if val == 0:
                    noZero -= 1
                left += 1
            ans = max(ans, right-left+1) 
        return ans