from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = len(t)
        if required > len(s):
            return ""
        t_map = defaultdict(int)
        for c in t:
            t_map[c] += 1
        right = 0
        left = 0
        min_len = float("inf")
        min_left_idx = 0
        matched = 0
        s_map = defaultdict(int)
        while right < len(s):
            right_char = s[right]
            s_map[right_char] += 1
            if s_map[right_char] == t_map[right_char]:
                matched += t_map[right_char]
            if matched == required:
                while left <= right:
                    left_char = s[left]
                    if right-left+1 < min_len:
                        min_len = right - left + 1
                        min_left_idx = left
                    s_map[left_char] -= 1
                    left += 1
                    if s_map[left_char] < t_map[left_char]:  
                        matched -= t_map[left_char]
                        break
            right += 1
        return "" if min_len == float("inf") else s[min_left_idx:min_left_idx+min_len]