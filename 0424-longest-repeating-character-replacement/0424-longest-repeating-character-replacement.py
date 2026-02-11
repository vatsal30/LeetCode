from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        freq = defaultdict(int)
        
        for right in range(len(s)):
            freq[s[right]] += 1

            # We only care about maximum frequency occured in array
            max_freq = max(freq[s[right]], max_freq)
            if (right - left + 1 - max_freq) > k:
                freq[s[left]]-=1
                left += 1

        return right - left + 1