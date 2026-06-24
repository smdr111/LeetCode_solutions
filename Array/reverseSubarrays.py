class Solution:
    def reverseSubarrays(self, nums: list[int], k: int) -> list[int]:
        l = len(nums)//k
        i = 0
        j = l
        res = []
        for _ in range(k):
            rev = nums[i:j][::-1]
            res += rev
            i += l
            j += l
        return res
    


        
