class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ans = []
        part_len = len(part)
        for c in s:
            ans.append(c)
           
            if c == part[-1] and len(ans) >= part_len:
                if ''.join(ans[-part_len:]) == part:
                    for _ in range(part_len):
                        ans.pop()
        return ''.join(ans)
                
                    
        