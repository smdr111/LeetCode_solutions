class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        x = 0  
        for i in range(n):
            res[i] = x
            x += nums[i]
        y = 0
        for i in range(n-1,-1,-1):
            res[i] = abs(res[i]-y)
            y += nums[i]
        return res


        return res
        

          

            

        
