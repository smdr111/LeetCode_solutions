class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        x = 0
        for i in sentences:
            if len(i.split()) > x:
                x = len(i.split())
        return x
