class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count0,count1,count2 = 0,0,0
        for i in stones:
            if i % 3 == 0:
                count0 += 1
            elif i % 3 == 1:
                count1 += 1
            else:
                count2 += 1
        if count0 % 2 == 0:
           return (count1 > 0 and count2 > 0)
        
        else:
            return abs(count1 - count2) > 2
    

            

        
