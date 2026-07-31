class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        count_list = sorted(counts.values(), reverse=True)
        return sum((i // 8 + 1) * count_list[i] for i in range(len(count_list)))
    
