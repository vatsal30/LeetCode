from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_c = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            max_c = max(max_c, freq[s[right]])

            if (right - left + 1) - max_c > k:
                freq[s[left]] -= 1
                left += 1
           
        return right - left + 1
            