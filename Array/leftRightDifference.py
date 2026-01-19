class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        total = sum(nums)
        left = 0
        for i in nums:
            right = total - left -i
            result.append(abs(left - right))
            left += i
        return result
