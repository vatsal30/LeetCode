class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == target:
                    return sums
                if abs(target - ans) > abs(target - sums):
                    ans = sums
                if target > sums:
                    j += 1
                else:
                    k -= 1
        return ans
