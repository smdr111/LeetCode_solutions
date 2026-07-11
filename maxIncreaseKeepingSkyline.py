class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        colmax = [0] * n
        for i in range(n):
            for j in range(n):
                colmax[i] = max(colmax[i],grid[j][i])
        ans = 0
        for i in range(n):
            rowmax = max(grid[i])
            for j in range(n):
                ans += min(rowmax,colmax[j]) - grid[i][j]
        return ans



        
            

            

        
