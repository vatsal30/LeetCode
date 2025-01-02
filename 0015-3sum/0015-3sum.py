class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = num + nums[j] + nums[k]
                if s == 0:
                    ans.append([num, nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k -1]:
                        k-= 1
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
        return ans

        