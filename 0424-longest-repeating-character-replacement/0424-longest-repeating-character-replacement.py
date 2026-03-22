from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_char = 0
        right = 0
        for right in range(len(s)):
            freq[s[right]] += 1
            max_char = max(max_char, freq[s[right]])

            if (right - left + 1) - max_char > k:
                freq[s[left]] -= 1
                left += 1
            
        return right - left + 1