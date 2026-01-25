from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # lookup = defaultdict(nums)
        ans = []
        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            idx1 = i + 1
            idx2 = len(nums) - 1

            while idx1 < idx2:
                total = nums[idx1] + nums[idx2] + num
                if total > 0:
                    idx2 -= 1
                elif total < 0:
                    idx1 += 1
                else:
                    ans.append([num, nums[idx1], nums[idx2]])
                    idx1 += 1
                    idx2 -= 1
                    while nums[idx1] == nums[idx1 - 1] and idx1 < idx2:
                        idx1 += 1
        return ans