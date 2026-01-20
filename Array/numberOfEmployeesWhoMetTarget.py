class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        i = 0
        for j in hours:
            if j >= target:
                i += 1
        return i

        
