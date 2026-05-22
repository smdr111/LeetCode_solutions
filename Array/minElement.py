class Solution:
    def minElement(self, nums: List[int]) -> int:
        x = []
        for i in nums:
            x.append(sum(int(j) for j in str(i)))
        return min(x)

           
        
