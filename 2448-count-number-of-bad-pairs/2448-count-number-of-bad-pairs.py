class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff = Counter([idx - nums[idx] for idx in range(n)])
        bad = n * (n-1) // 2
        good = 0
        for good_pair in diff.values():
            bad -= (good_pair) * (good_pair - 1) // 2
        return bad
