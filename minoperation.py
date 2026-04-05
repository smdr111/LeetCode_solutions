class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        i = 0
        for j in nums:
            if j < k:
                i += 1
        return i

            
     
        
        
