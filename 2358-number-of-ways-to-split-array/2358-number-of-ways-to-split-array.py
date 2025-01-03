class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = 0
        for num in nums:
            s += num
        ans = 0
        t = 0
        for idx in range(len(nums) - 1):
            t += nums[idx]
            s -= nums[idx]
            if t >= s:
                ans += 1
        return ans