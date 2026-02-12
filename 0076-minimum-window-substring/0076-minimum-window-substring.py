from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_map = Counter(t)
        required = len(t_map)
        left, right = 0, 0
        min_len = float("inf")
        min_left_idx = 0
        formed = 0
        s_map = defaultdict(int)
        while right < len(s):
            right_char = s[right]
            s_map[right_char] += 1
            if s_map[right_char] == t_map[right_char]:
                formed += 1
            if formed == required:
                while left <= right:
                    left_char = s[left]
                    if right-left+1 < min_len:
                        min_len = right - left + 1
                        min_left_idx = left
                    s_map[left_char] -= 1
                    left += 1
                    if s_map[left_char] < t_map[left_char]:  
                        formed -= 1
                        break
            right += 1
        return "" if min_len == float("inf") else s[min_left_idx:min_left_idx+min_len]