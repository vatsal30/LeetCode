class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if num - 1 not in num_set:
                seq = 1
                while num + seq in num_set:
                    seq += 1
                ans = max(ans, seq)
        return ans
