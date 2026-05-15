from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        m = len(s)
        if n > m:
            return ""
        t_dict = Counter(t)
        s_dict = defaultdict(int)
        left = 0
        have = 0
        needed = len(t_dict)
        ans = (0, float("inf"))

        for right in range(m):
            right_c = s[right]
            s_dict[right_c] += 1
            if right_c in t_dict and t_dict[right_c] == s_dict[right_c]:
                have += 1
            
            while have == needed:
                if (ans[1] - ans[0]) > right - left:
                    ans = (left, right)
                left_c = s[left]
                s_dict[left_c] -= 1
                if left_c in t_dict and s_dict[left_c] < t_dict[left_c]:
                    have -= 1
                left += 1
        
        return s[ans[0]: ans[1] + 1] if ans[1] != float("inf") else ""