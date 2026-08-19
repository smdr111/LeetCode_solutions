class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        totals = []
        for i in bank:
            count = i.count('1')
            if count != 0:
                totals.append(count)
        n = len(totals)
        if n == 1:
            return 0
        ans = 0
        for i in range(n-1):
            ans += (totals[i] * totals[i+1])
        return ans
        



        
        
