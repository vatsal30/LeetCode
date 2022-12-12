class Solution:
    def bfs(self, sr, sc, floodFill, image, deltaRow, deltaCol, initColor, newColor):
        floodFill[sr][sc] = newColor
        queue = []
        queue.append((sr, sc))
        
        n = len(image)
        m = len(image[0])
        while(queue):
            row, col = queue.pop(0)
            for i in range(4):
                updatedRow = row + deltaRow[i]
                updatedCol = col + deltaCol[i]
                
                if (updatedRow>=0 and updatedRow<n and updatedCol>=0 and updatedCol<m and 
                    image[updatedRow][updatedCol]==initColor and floodFill[updatedRow][updatedCol]!=newColor):
                    floodFill[updatedRow][updatedCol] = newColor
                    queue.append((updatedRow, updatedCol))
                    
    
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		floodFill = image
		initColor = image[sr][sc]
		deltaRow = [-1, 0, 1, 0]
		deltaCol = [0, 1, 0, -1]
		
		self.bfs(sr, sc, floodFill, image, deltaRow, deltaCol, initColor, newColor)
        return floodFill


#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends