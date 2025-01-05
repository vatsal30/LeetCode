class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for idx in range(n):
            prod = nums[idx]
            gcd = nums[idx]
            lcm = nums[idx]
            temp = 0
            for k in range(idx + 1, n):
                prod *= nums[k]
                gcd = math.gcd(nums[k], gcd)
                lcm = math.lcm(lcm, nums[k])
                if prod > 2520:
                    break
                if prod ==  gcd*lcm :
                    temp = (k - idx) + 1
            ans = max(temp, ans)
        return ans


        