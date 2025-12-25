class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x = set(range(len(nums)+1))-set(nums)
        return x.pop()
        
        
