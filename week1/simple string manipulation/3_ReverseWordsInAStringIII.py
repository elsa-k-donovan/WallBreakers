class Solution:
    def reverseWords(self, s: str) -> str:
        
        #Split into separate words
        newList = s.split()
    
        totalList = []
        
        for i in newList:
            #print(i)
            tmp = list(i)
            tmp.reverse()
            tmp = ''.join(tmp)
            totalList.append(tmp)
        
        tre = ' '.join(totalList)
        return tre
