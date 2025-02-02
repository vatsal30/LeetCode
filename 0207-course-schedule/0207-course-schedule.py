class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = { i: [] for i in range(numCourses)}
        inDeg = [0] * numCourses
        for course, req in prerequisites:
            inDeg[course] += 1
            preReq[req].append(course)
        
        queue = deque([idx for idx, val in enumerate(inDeg) if val == 0])
        
        courseCanTake = 0
        
        while queue:
            course = queue.popleft()
            courseCanTake += 1
            for nextCourse in preReq[course]:
                inDeg[nextCourse] -= 1
                if inDeg[nextCourse] == 0:
                    queue.append(nextCourse)
        return courseCanTake == numCourses
        