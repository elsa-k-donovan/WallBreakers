class Solution:
    def titleToNumber(self, s: str) -> int:

        total = 0
        value = list(str(s))
        size = len(value)

        count = 0
        
        
        while(len(value) > 0):
            
            total = total + (ord(value[-1])-64)*(26**count)

            del(value[-1])
            
            count += 1
            
        return total
