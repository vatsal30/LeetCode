from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        prereq_graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            prereq_graph[prereq].append(course)
            indegree[course] += 1        
        q = deque()
        for course, degree in enumerate(indegree):
            if degree == 0:
                q.append(course)
        while q:
            course = q.popleft()
            for  dependent in prereq_graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)
        for degree in indegree:
            if degree:
                return False
        return True