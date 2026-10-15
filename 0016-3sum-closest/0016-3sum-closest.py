class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        ans = -1
        for i in range(len(nums) - 2): 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                diff = abs(target - sums)
                if closest > diff:
                    closest = diff
                    ans = sums
                if target > sums:
                    j += 1
                else:
                    k -= 1
        return ans
