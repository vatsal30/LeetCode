class Solution:
    def sumOfDigits(self, num: int) -> int:
        ans = 0
        while num > 0:
            ans += num % 10
            num = num // 10
        return ans

    def maximumSum(self, nums: List[int]) -> int:
        nums.sort()
        lookup = {}
        ans = -1
        for num in nums:
            digit_sum = self.sumOfDigits(num)
            if digit_sum in lookup:
                ans = max(num + lookup[digit_sum], ans)
            lookup[digit_sum] = num
        return ans