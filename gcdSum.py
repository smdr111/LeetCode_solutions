class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = []
        prefixMax = -inf

        for x in nums:
            prefixMax = max(prefixMax, x)
            mx.append(prefixMax)

        prefix_gcd = [gcd(x, y) for x, y in zip(nums, mx)]
        prefix_gcd.sort()

        ans = 0
        left, right = 0, n - 1
        for _ in range(n//2):
            ans += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        return ans

