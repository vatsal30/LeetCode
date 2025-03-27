class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def helper(i, mw):
            if i >= len(s):
                return True
            if i + len(mw) >= len(s) and s[i:i+len(mw)] != mw:
                return False
            if s[i:i+len(mw)] == mw:
                for word in wordDict:
                    if helper(i+len(mw), word):
                        return True
            return False
        
        for word in wordDict:
            if helper(0, word):
                return True
        return False