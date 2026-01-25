from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # lookup = defaultdict(nums)
        ans = set()
        for i in range(len(nums)):
            target = nums[i]
            idx1 = i + 1
            idx2 = len(nums) - 1

            while idx1 < idx2:
                total = nums[idx1] + nums[idx2] + target
                if total > 0:
                    idx2 -= 1
                elif total < 0:
                    idx1 += 1
                else:
                    ans.add((nums[i], nums[idx1], nums[idx2]))
                    idx1 += 1
                    idx2 -= 1
        return list(ans)