class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        # This is because there are only 26 letters, so a max of 26 odd occurences.
        if k >= 26:
            return True
        freq_map = Counter(s)
        oneCount = 0
        for letter in freq_map:
            if freq_map[letter]%2 == 1:
                oneCount += 1
                if oneCount > k:
                    return False
        return True
        # oneCount = sum(i % 2 == 1 for i in range)