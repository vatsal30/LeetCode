class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            valid = True
            while asteroid < 0 and stack and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    valid = False
                    break
                else:
                    valid = False
                    break
            if valid:
                stack.append(asteroid)
        return stack