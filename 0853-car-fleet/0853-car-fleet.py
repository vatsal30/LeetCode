class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for i in range(len(cars)):
            time_to_complete = (target - cars[i][0]) / cars[i][1]
            stack.append(time_to_complete)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        # print(stack)
        return len(stack)