class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        if len(tasks)==1:
            return sum(tasks[0])
        result = sum(tasks[0])
        for task in tasks[1:]:
            n = sum(task)
            if n < result:
                result = n

        return result
