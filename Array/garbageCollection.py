class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = len(''.join(garbage))
        prefix = [0] * len(garbage)
        for i in range(1, len(garbage)):
            prefix[i] = prefix[i - 1] + travel[i - 1]
        for ch in 'MPG':
            last = -1
            for i, g in enumerate(garbage):
                if ch in g:
                    last = i
            if last != -1:
                total += prefix[last]

        return total

            




            

        
        
