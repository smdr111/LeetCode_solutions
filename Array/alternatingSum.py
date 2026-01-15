class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = 0
        for i in range(1,len(nums),2):
            x += nums[i]
        
        y = 0
        for j in range(0,len(nums),2):
            y += nums[j]
        
        return y-x

        
