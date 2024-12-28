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
        dp = [[0] * (2 * totalSum + 1) for _ in range(len(nums))]
        dp[0][nums[0] + totalSum] = 1
        dp[0][-nums[0] + totalSum] += 1
        for idx in range(1, len(nums)):
            for sum_val in range(-totalSum, totalSum + 1):
                if dp[idx-1][sum_val + totalSum] > 0:
                    dp[idx][sum_val + nums[idx] + totalSum] += dp[idx-1][sum_val + totalSum]
                    dp[idx][sum_val - nums[idx] + totalSum] += dp[idx-1][sum_val + totalSum]
        return 0 if abs(target) > totalSum else dp[len(nums) -1][target + totalSum]

        