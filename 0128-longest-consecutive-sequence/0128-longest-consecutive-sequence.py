class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        ans = 0
        for num in uniq_nums:
            if num - 1 not in uniq_nums:
                seq = 1
                while num + seq in uniq_nums:
                    seq += 1
                ans = max(ans, seq)
        return ans