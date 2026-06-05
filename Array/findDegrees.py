class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans = [sum(i) for i in matrix]
        return ans
