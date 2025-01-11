class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        freq_map = Counter(s)
        oneCount = 0
        for letter in freq_map:
            if freq_map[letter]%2 == 1:
                oneCount += 1
        if oneCount > k:
            return False
        return True
        # oneCount = sum(i % 2 == 1 for i in range)