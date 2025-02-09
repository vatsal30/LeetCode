class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff_map = defaultdict(int)
        ans = 0
        mod = 10**9 + 7
        for num in nums:
            diff = num - int(str(num)[::-1])
            diff_map[diff] += 1
            ans = (ans + diff_map[diff] - 1) % mod
        return ans


