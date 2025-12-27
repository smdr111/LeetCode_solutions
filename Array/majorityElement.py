import random as r
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        while nums:
            i = r.choice(nums)
            if nums.count(i) > n:
                return i 
                break
        
       
        
