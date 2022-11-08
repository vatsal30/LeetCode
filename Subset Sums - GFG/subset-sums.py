#User function Template for python3
class Solution:
    def computeSum(self, idx, ds_sum, arr, N, answer):
        if (idx == N):
            answer.append(ds_sum)
            return
        self.computeSum(idx+1, ds_sum + arr[idx], arr, N, answer)
        self.computeSum(idx+1, ds_sum, arr, N, answer)
        

	def subsetSums(self, arr, N):
		# code here
        answer = []
        self.computeSum(0, 0, arr, N, answer)
        answer.sort()
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends