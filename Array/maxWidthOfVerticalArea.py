class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_values = sorted([i[0] for i in points])
        ans = 0
        for i in range(len(x_values)-1):
            ans = max(ans,x_values[i+1] - x_values[i])
        return ans
