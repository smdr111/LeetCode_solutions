class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {}
        word = 'balloon'
        for c in text:
            if c in word:
                counts[c] = counts.get(c,0) + 1
        if len(counts) == 5:
            if counts['l'] >= 2 and counts['o'] >= 2:
                return min(
                    counts['b'],
                    counts['a'],
                    counts['l'] // 2,
                    counts['o'] // 2,
                    counts['n']
                )
        return 0
            


