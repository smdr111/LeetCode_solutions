class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        rowOnes = [sum(grid[i]) for i in range(m)]
        colOnes = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = 2 * rowOnes[i] + 2 * colOnes[j] - m - n
        return result



        

        
