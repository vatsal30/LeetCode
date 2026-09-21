class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        prereq_graph = [[] for _ in range(numCourses)]
        order = []

        for course, prereq in prerequisites:
            indegree[course] += 1
            prereq_graph[prereq].append(course)
        
        q = deque()
        for course, degree in enumerate(indegree):
            if degree == 0:
                q.append(course)
        
        while q:
            course = q.popleft()
            for dependent in prereq_graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    q.append(dependent)

            order.append(course)
        
        return order if len(order) == numCourses else []