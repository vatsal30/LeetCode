#User function Template for python3

class Solution:
    def solvePath(self, row, col, m, n, ans, path, visited_m):
        if (row == n-1 and col == n-1):
            ans.append(path)
            return
        # Down
        if (row+1<n and m[row+1][col]==1 and visited_m[row+1][col]==0):
            visited_m[row][col]=1
            self.solvePath(row+1, col, m, n, ans, path + "D", visited_m)
            visited_m[row][col]=0
        
        # Left
        if (col-1>=0 and m[row][col-1]==1 and visited_m[row][col-1]==0):
            visited_m[row][col]=1
            self.solvePath(row, col-1, m, n, ans, path + "L", visited_m)
            visited_m[row][col]=0
        
        # Right
        if (col+1<n and m[row][col+1]==1 and visited_m[row][col+1]==0):
            visited_m[row][col]=1
            self.solvePath(row, col+1, m, n, ans, path + "R", visited_m)
            visited_m[row][col]=0
            
        # Up
        if (row-1>=0 and m[row-1][col]==1 and visited_m[row-1][col]==0):
            visited_m[row][col]=1
            self.solvePath(row-1, col, m, n, ans, path + "U", visited_m)
            visited_m[row][col]=0

    def findPath(self, m, n):
        # code here
        ans = []
        visited_m = [[0 for i in range(n)] for j in range(n)]
        
        if (m[0][0] == 1):
            self.solvePath(0, 0, m, n, ans, "", visited_m)
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends