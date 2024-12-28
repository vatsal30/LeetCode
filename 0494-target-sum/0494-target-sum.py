'''
Time limit Exceeded burte force solution

class Solution:
    def __init__(self):
        self.ans = 0

    def solve(self, nums, target, curr, idx):
        if idx == len(nums):
            if target == curr:
                self.ans += 1
            return
        self.solve(nums, target, curr + nums[idx], idx + 1)
        self.solve(nums, target, curr - nums[idx], idx + 1)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.solve(nums, target, 0, 0)
        return self.ans
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        dp = [0] * (2 * totalSum + 1)
        dp[nums[0] + totalSum] = 1
        dp[-nums[0] + totalSum] += 1
        for idx in range(1, len(nums)):
            new_dp = [0] * (2 * totalSum + 1)
            for sum_val in range(-totalSum, totalSum + 1):
                if dp[sum_val + totalSum] > 0:
                    new_dp[sum_val + nums[idx] + totalSum] += dp[sum_val + totalSum]
                    new_dp[sum_val - nums[idx] + totalSum] += dp[sum_val + totalSum]
            dp = new_dp
        return 0 if abs(target) > totalSum else dp[target + totalSum]

        