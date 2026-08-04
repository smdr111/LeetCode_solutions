class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        n = min(nums)
        m = max(nums)
        return [i for i in range(n,m+1) if i not in set_nums]

        

        
        
