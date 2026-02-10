from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        left = 0
        right = 0
        freq = defaultdict(int)
        ans = 0
        while right < len(s):
            freq[s[right]] += 1
            max_freq = max(freq[s[right]], max_freq)
            if (right - left + 1 - max_freq) <= k:
                ans = max(ans, right - left + 1)
            else:
                freq[s[left]]-=1
                left += 1
                
            right += 1
        return ans