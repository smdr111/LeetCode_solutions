class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for char in s:
            if char == '*' :
                if res:
                    res.pop()
            elif char == '#':
                res *= 2
            elif char == '%':
                res = res[::-1]
            else :
                res.append(char)
        return ''.join(res)



        
