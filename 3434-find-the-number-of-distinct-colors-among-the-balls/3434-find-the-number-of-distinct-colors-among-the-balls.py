class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        colors = defaultdict(set)
        ans = []
        for ball, color in queries:
            if ball in balls:
                pre_color = balls[ball]
                balls[ball] = color
                colors[pre_color].remove(ball)
                if len(colors[pre_color]) == 0:
                    del colors[pre_color] 
                colors[color].add(ball)
            else:
                colors[color].add(ball)
                balls[ball] = color
            ans.append(len(colors.keys()))
        return ans
