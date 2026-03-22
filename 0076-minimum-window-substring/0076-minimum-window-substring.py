from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        right = 0
        left = 0
        t_freq = {}
        s_freq = defaultdict(int)
        ans = (0, float("inf"))
        needed = len(t)
        have = 0

        for i in range(needed):
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1
        
        for right in range(len(s)):
            right_char = s[right]
            s_freq[right_char] += 1
            char_freq = s_freq[right_char]
            
            if right_char in t_freq and char_freq == t_freq[right_char]:
                have += char_freq
            
            while have == needed and left <= right:
                if ((ans[1] - ans[0]) > (right - left)):
                    ans = (left, right)

                left_char = s[left]
                s_freq[left_char] -= 1 
                if left_char in t_freq and s_freq[left_char] < t_freq[left_char]:
                    have -= t_freq[left_char]
                left += 1    
        return s[ans[0]:ans[1]+1] if ans[1] != float("inf") else ""