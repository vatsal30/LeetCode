class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += ans
            if digits[i] > 9:
                ans = 1
                digits[i] %= 10
            else:
                ans = 0
                break
        if ans:
            digits = [1] + digits
        return digits