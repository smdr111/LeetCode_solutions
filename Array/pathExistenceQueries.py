class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n
        current = 0
        for i in range(1,n):
            if (nums[i] - nums[i-1]) <= maxDiff:
                component[i] = current
            else:
                current += 1
                component[i] = current
        ans = [component[i]==component[j] for i,j in queries]
        return ans
