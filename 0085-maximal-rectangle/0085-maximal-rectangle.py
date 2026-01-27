class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        arr = [0] * (len(matrix[0]) + 1) 
        for i in range(len(matrix)):
            stack = [-1]
            for idx in range(len(matrix[i])):
                if matrix[i][idx] == "0":
                    arr[idx] = 0
                else:
                    arr[idx] += 1
            for idx in range(len(arr)):
                while stack[-1] != -1 and arr[stack[-1]] > arr[idx]:
                    height = arr[stack.pop()]
                    width = idx - stack[-1] - 1
                    result = max(result, height*width)
                stack.append(idx)
        return result