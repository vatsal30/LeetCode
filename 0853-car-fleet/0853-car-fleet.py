class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse= True)
        stack = []
        for pos, s in cars:
            time = (target - pos) / s
            if not stack or stack[-1] < time:
                stack.append(time)
        return len(stack)