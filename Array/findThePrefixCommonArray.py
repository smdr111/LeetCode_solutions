class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        for i in range(len(A)):
            result.append(len(set(A[:i+1])&set(B[:i+1])))

        return result
        
