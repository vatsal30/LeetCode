class Solution:
    def dfs(self, closeCount: int, openCount: int, curr: str,  ans:List[str]):
        if closeCount == 0 and openCount == 0:
            ans.append(curr)
            return 
        if openCount != 0:
            self.dfs(closeCount, openCount-1, curr + "(", ans)
        if openCount < closeCount:
            self.dfs(closeCount - 1, openCount, curr + ")", ans)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, n, "", ans)
        return ans
        