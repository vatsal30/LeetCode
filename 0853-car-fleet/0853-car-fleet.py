class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pair in cars:
            time_to_complete = (target - pair[0]) / pair[1]
            stack.append(time_to_complete)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # print(stack)
        return len(stack)