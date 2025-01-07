class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x))
        n = len(words)
        ans = []
        for idx in range(n):
            for j in range(idx + 1, n):
                if len(words[j]) == len(words[idx]):
                    continue
                if words[idx] in words[j]: 
                    ans.append(words[idx])
                    break
        return ans