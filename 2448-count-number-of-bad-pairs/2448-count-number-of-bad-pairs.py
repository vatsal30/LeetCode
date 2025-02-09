class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        ans = 0
        diff = defaultdict(int)
        n = len(nums)
        total = n * (n-1) // 2
        good = 0
        for idx, num in enumerate(nums):
            curr_diff = num - idx
            diff[curr_diff] += 1
            good += (diff[curr_diff] - 1) 
        return total - good
