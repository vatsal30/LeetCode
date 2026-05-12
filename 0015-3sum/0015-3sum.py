class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
    
            while nums[i] == nums[i + 1] and i < len(nums) - 2:
                i += 1
            i += 1
        return ans