class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = mx = nums[0]
        for x in nums[1:]:
            if x < mn:
                mn = x
            elif x > mx:
                mx = x
        return gcd(mn, mx)
        
