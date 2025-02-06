class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        prefixProd = 1
        for idx in range(n):
           ans[idx] *= prefixProd
           prefixProd *= nums[idx]
        suffixProd = 1
        for idx in range(n-1, -1, -1):
            ans[idx] *= suffixProd
            suffixProd *= nums[idx]
        return ans