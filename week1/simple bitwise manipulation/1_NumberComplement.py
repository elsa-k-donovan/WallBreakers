class Solution:
    def findComplement(self, num: int) -> int:
        
        binary = format(num, 'b')
        print(binary)
        
        s = list(binary)
        
        newlist = []
        
        for i in s:
            if i == '1':
                newlist.append('0')
            else:
                newlist.append('1')
                
                
        print(newlist)
        
        tmp = ''.join(newlist)
        z = int(tmp, 2)
        
        return z
