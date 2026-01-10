class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        i = 0
        for j in operations:
            if j == '--X' or j == 'X--':
                i -= 1
            else:
                i += 1
        return i
        
        

        
