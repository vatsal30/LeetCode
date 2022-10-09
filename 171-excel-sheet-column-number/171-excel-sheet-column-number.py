class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ascii_diff = 64
        multiplier = 0
        colNumber = 0
        for i in reversed(columnTitle):
            colNumber += (26 ** multiplier) * (ord(i) - ascii_diff)
            multiplier += 1
        return colNumber