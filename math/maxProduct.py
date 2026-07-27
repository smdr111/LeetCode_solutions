class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        x,y = 0,0
        for i in nums:
            if i > x:
                y = x
                x = i
            elif i >= y:
                y = i
        return (x-1) * (y-1)

        
