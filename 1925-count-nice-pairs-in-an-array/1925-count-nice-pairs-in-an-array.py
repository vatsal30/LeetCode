class Solution:
    def reverse_number(self, n):
        r = 0
        while n > 0:
            r *= 10
            r += n % 10
            n //= 10
        return r

    def countNicePairs(self, nums: List[int]) -> int:
        diff_map = defaultdict(int)
        ans = 0
        mod = 10**9 + 7
        for num in nums:
            diff = num - int(str(num)[::-1])
            diff_map[diff] += 1
            ans = (ans + diff_map[diff] - 1) % mod
        return ans


