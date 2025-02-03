class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = float("-inf")
        max_dec = float("-inf")
        idx = 2
        if len(nums) == 1:
            return 1
        is_inc = nums[1] > nums[0]
        is_dec = nums[1] < nums[0]
        count = 1 if is_inc or is_dec else 0
        while idx < len(nums):
            if nums[idx] > nums[idx-1]:
                if is_inc:
                    count += 1
                elif is_dec:
                    max_dec = max(max_dec, count)
                    is_dec = False
                    is_inc = True
                    count = 1
                else:
                    count = 1
                    is_inc = True
            elif nums[idx] < nums[idx-1]:
                if is_dec:
                    count += 1
                elif is_inc:
                    max_inc = max(max_inc, count)
                    is_inc = False
                    is_dec = True
                    count = 1
                else:
                    is_dec = True
                    count = 1
            else:
                if is_inc:
                    max_inc = max(max_inc, count)
                elif is_dec:
                    max_dec = max(max_dec, count)
                count = 0
                is_inc = 0
                is_dec = 0
            idx += 1
        if is_inc:
            max_inc = max(max_inc, count)
        else:
            max_dec = max(max_dec, count)
        return max(max_inc, max_dec) + 1