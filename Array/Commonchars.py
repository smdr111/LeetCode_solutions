from collections import Counter
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])          # birinchi so‘zdagi harflar soni
        for w in words[1:]:
            common &= Counter(w)            # min chastota bo‘yicha kesishma
        return list(common.elements())
        
            


        
