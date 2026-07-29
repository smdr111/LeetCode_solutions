class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)

        base = sorted(s[:n//2])
        mid = [] if n % 2 == 0 else [s[n//2]]
        last = base[::-1]
        return "".join(base + mid + last)
        


        
