class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # O(1) solution using pascal's triangle formula
        # ans = [1]
        # for i in range(1, rowIndex + 1):
        #    ans.append(ans[-1] * (rowIndex - i + 1) // i)
        # return ans
        ans = [1]
        for i in range(1, rowIndex + 1):
            ans = [0] + ans + [0]
            for j in range(i + 1):
                ans[j] += ans[j+1]
            ans = ans[:-1]
        return ans