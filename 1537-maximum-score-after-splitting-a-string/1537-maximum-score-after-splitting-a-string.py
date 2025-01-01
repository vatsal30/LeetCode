class Solution:
    def maxScore(self, s: str) -> int:
        one_sum = 0
        for c in s:
            one_sum += int(c)
        max_val = float("-inf")
        zero_sum = 0
        for c in s[:-1]:
            if c == '0':
               zero_sum += 1
            else:
                one_sum -= 1
            max_val = max(zero_sum + one_sum, max_val)

        return max_val
            