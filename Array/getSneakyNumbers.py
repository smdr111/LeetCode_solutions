from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dupes = [x for x, c in Counter(nums).items() if c > 1]
        return dupes
        
