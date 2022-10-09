class Solution:
    def romanToInt(self, s: str) -> int:
        romanSymbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        convertedVal = [1, 5, 10, 50, 100, 500, 1000]
        prevIdx = 10
        number = 0
        for i in range(0, len(s)):
            idx = romanSymbol.index(s[i])
            if (idx > prevIdx):
                number = number - (2 * convertedVal[prevIdx]) + convertedVal[idx]
            else:
                number = number + convertedVal[idx]
            prevIdx = idx
        return number