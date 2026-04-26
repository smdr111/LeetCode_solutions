class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for index,letter in enumerate(s):
            res[indices[index]] = letter

        return "".join(res)



        
        
           

        
