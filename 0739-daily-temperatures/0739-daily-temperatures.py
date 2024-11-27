class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stack = []
        for temp in reversed(temperatures):
            if len(stack) == 0:
                ans.append(0)
                stack.append((temp, 0))
                continue
            if temp < stack[-1][0]:
                ans.append(1)
                stack.append((temp,1))
            else:
                ele = stack.pop()
                count = ele[1]
                while len(stack) and stack[-1][0] <= temp:
                    ele = stack.pop(-1)
                    count += ele[1]
                if len(stack):
                    stack.append((temp, count + 1))
                    ans.append(count + 1)
                else:
                    stack.append((temp, 0))
                    ans.append(0)
        return list(reversed(ans))

        