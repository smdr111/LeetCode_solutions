class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        x = inf
        y = 0
        for i in nums:
            if i > y:
                y = i
            if i < x:
                x = i
        return (y - x) * k
