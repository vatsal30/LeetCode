class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReq = { i: [] for i in range(numCourses)}
        inDeg = [0] * numCourses
        for course, req in prerequisites:
            inDeg[course] += 1
            preReq[req].append(course)
        
        queue = deque([idx for idx, val in enumerate(inDeg) if val == 0])
        
        courseOrder = []
        
        while queue:
            course = queue.popleft()
            courseOrder.append(course)
            for nextCourse in preReq[course]:
                inDeg[nextCourse] -= 1
                if inDeg[nextCourse] == 0:
                    queue.append(nextCourse)
        return courseOrder if len(courseOrder) == numCourses else []
        
        