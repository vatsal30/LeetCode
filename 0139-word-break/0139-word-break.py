# class TrieNode:
#     def __init__(self):
    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = {}
        end_symbol = "*"
        for word in wordDict:
            curr = root
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr[end_symbol] = True
        
        dp = [False] * len(s)
        for idx in range(len(s)):
            if idx == 0 or dp[idx - 1]:
                curr = root
                for j in range(idx, len(s)):
                    if s[j] not in curr:
                        break
                    curr = curr[s[j]]
                    if end_symbol in curr:
                        dp[j] = True
        return dp[-1]