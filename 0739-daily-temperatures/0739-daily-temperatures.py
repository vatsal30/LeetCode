class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while temp_stack and temperatures[temp_stack[-1]] < temp:
                prev_idx = temp_stack.pop()
                ans[prev_idx] = idx - prev_idx
            temp_stack.append(idx)
        return ans