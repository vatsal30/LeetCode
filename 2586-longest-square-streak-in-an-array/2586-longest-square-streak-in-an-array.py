class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numSet= set(nums)
        ans = -1
        nums.sort()
        for i in nums[:318]:
            num = i
            count = 0
            while num ** 2 in numSet:
                count += 1
                num **= 2
            if count != 0:
                ans = max(ans, count+1)
        return ans