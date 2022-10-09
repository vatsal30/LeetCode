class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0
        for w in words:
            idx = 0
            flag = True
            for ch in w:
                idx = s.find(ch, idx)
                if (idx == -1):
                    flag=False
                    break
                idx += 1
            if (flag):
                count+=1
        return count