class Solution:
    def (self, nums: List[int]) -> int:
        i = 0
        for j in nums:
            if j%3!=0:
                i+=1
        return i
        
