class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openC = 0
        ans = list(s)
        for idx, letter in enumerate(s):
            if letter == '(':
                openC += 1
            elif letter == ')':
                if openC:
                    openC -= 1
                else:
                    ans[idx] = ''
        idx = len(s) - 1
        while idx >=0 and openC:
            if ans[idx] == '(':
                ans[idx] = ''
                openC -= 1
            idx -= 1
        return "".join(ans)
        

            
        