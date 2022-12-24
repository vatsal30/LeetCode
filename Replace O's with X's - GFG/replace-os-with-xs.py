#User function Template for python3

class Solution:
    def dfs(self, row, col, n, m, mat, vis):
        vis[row][col] = 1

        delRow = [-1, 0, 1, 0]
        delCol = [0, -1, 0, 1]
        
        for i in range(4):
            nRow = row + delRow[i]
            nCol = col + delCol[i]
            
            if(nRow>=0 and nRow<n and nCol>=0 and nCol<m and (not vis[nRow][nCol]) and mat[nRow][nCol]=='O'):
                self.dfs(nRow, nCol, n, m, mat, vis)
        
    def fill(self, n, m, mat):
        # code here
        vis = [[0 for i in range(m)] for j in range(n)]
        
        for i in range(n):
            if(not vis[i][0] and mat[i][0] == 'O'):
                self.dfs(i, 0, n, m, mat, vis)
            if(not vis[i][m-1] and mat[i][m-1] == 'O'):
                self.dfs(i, m-1, n, m, mat, vis)
        
        for j in range(m):
            if(not vis[0][j] and mat[0][j] == 'O'):
                self.dfs(0, j, n, m, mat, vis)
            if(not vis[n-1][j] and mat[n-1][j] == 'O'):
                self.dfs(n-1, j, n, m, mat, vis)
            
        for i in range(n):
            for j in range(m):
                if(not vis[i][j] and mat[i][j]=='O'):
                    mat[i][j] = 'X'
        
        return mat 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends