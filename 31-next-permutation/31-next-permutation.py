class Solution:
    def reverse(self, nums, start, end):
        while(start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
    
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = len(nums)-2
        while (nums[k]>=nums[k+1]) and k>=0:
            k-=1
        if (k<0):
            return nums.reverse()
        for i in range(len(nums)-1, -1, -1):
            if (nums[i] > nums[k]):
                nums[i], nums[k] = nums[k], nums[i]
                self.reverse(nums,k+1,len(nums)-1)
                break
        return  nums