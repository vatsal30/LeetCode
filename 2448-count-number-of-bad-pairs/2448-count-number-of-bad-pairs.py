class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        diff = Counter([idx - nums[idx] for idx in range(n)])
        total = n * (n-1) // 2
        good = 0
        for good_pair in diff.values():
            good += (good_pair) * (good_pair - 1) // 2
        return total - good
