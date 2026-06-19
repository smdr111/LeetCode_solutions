class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        start = 0
        res = 0
        for i in range(n):
            start += gain[i]
            if start > res:
                res = start
        return res



        
