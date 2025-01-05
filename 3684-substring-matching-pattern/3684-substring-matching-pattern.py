class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        pat = p.split('*')
        if pat[0] not in s:
            return False
        idx1 = s.index(pat[0]) if pat[0] else 0
        if pat[1] in s[idx1 + len(pat[0]):]:
            return True
        return False