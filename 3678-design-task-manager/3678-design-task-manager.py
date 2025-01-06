class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_queue = []
        self.task_map = {}
        self.UNKNOWN = -1
        for task in tasks:
            task.reverse()
            task[0] = -task[0]
            task[1] = -task[1]
            self.task_map[-task[1]] = task
            heapq.heappush(self.task_queue, task)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = [-priority, -taskId, userId]
        heapq.heappush(self.task_queue, task)
        self.task_map[taskId] = task

    def edit(self, taskId: int, newPriority: int) -> None:
        task = self.task_map.pop(taskId)
        userId = task[-1]
        new_task = [-newPriority, -taskId, userId]
        task[-1] = self.UNKNOWN
        self.task_map[taskId] = new_task
        heapq.heappush(self.task_queue, new_task)

    def rmv(self, taskId: int) -> None:
        task = self.task_map.pop(taskId)
        task[-1] = self.UNKNOWN
        
    def execTop(self) -> int:
        while self.task_queue:
            task = heapq.heappop(self.task_queue)
            if task[-1] is not self.UNKNOWN:
                del self.task_map[-task[1]]
                return task[2]
        return -1
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()