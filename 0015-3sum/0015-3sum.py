class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        i = 0
        n = len(nums) - 1
        ans = list()
        for i in range(n):
            if nums[i] > 0:
                break
        
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j = i + 1
            k = n
            while j < k:
                currSum = nums[j] + nums[k]
                if currSum == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif currSum < -nums[i]:
                    j += 1
                else:
                    k -= 1
            
        return ans