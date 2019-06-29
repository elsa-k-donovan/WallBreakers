class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
      
        goodList = []
        newList = []    
            
        for x in range (left, right+1):
            A = list(str(x))
        
            if ("0" in A):
                None
                
            else:
                for y in A:
                    
                    if(x % eval(y) != 0):
                        break
                    if(x % eval(y) == 0):
                        goodList.append(x)
                        
            
        for z in goodList:
            count = goodList.count(z)
            if (len(str(z)) == count) and (z not in newList):
                newList.append(z)
        
        return newList
