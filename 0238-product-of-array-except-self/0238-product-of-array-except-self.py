class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        prod_till_left = 1
        leftMap = [1] * N
        for i in range(N):
            leftMap[i] = prod_till_left
            prod_till_left *= nums[i]
        
        prod_till_right = 1
        for i in range(N-1,-1,-1):
            leftMap[i] *= prod_till_right
            prod_till_right *= nums[i]
        
        return leftMap