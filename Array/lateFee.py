class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        result = []
        for i in daysLate:
            if i==1:
                result.append(1)
            elif 2 <= i <= 5:
                result.append(2*i)
            elif i > 5:
                result.append(3*i)
        return sum(result)
        
