class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        diff = Counter()
        for idx, num in enumerate(nums):
            curr_diff = num - idx
            diff[curr_diff] += 1
            ans += (idx + 1) - diff[curr_diff]
        return ans
