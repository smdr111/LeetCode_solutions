class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seat = sorted(seats)
        student = sorted(students)
        x = 0
        for i in range(len(seat)):
            x += abs(seat[i]-student[i])
        return x
        
