class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        x = 0 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    x += 1
            result.append(x)
            x = 0
        return result
            
                    



        
