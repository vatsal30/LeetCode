class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        diff = defaultdict(int)
        for idx, num in enumerate(nums):
            diff[num - idx] += 1
            ans += (idx + 1) - diff[num - idx]
        return ans
