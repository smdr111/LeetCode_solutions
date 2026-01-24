class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        d = defaultdict(set)
        for student, bench in students:
            d[bench].add(student) 

        return max(map(len, d.values()), default = 0) 


        
