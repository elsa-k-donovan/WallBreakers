class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        #convert to binary
      #  binaryX = format(x, '04b')
      #  binaryY = format(y, '04b')
        
        #convert to binary but it includes '0b' 
        
        #copies bit if it is set in one operand but not the other
        binaryX = bin(x)
        binaryY = bin(y)
        c = x^y
        binaryC = bin(c)
        
        countC = binaryC.count('1')
        return countC
        
        #.count to count the 1s
       # print(binaryX)
        
      #  listX = list(binaryX)
     #   listY = list(binaryY)
            
            
        #look up bin() function
        #carrot function
        #.count(1)
        #count = 0
        
        #if listY > listX:
      #  for i in range(len(listX)):
               # if listX[i] != listY[i]:
                 #   count += 1
        #else:
         #   for itemX in listX:
           #     for itemY in listY:
           #         if itemX != itemY:
               #         count += 1
    
    """
        #find longest list
        if listY > listX:
            return (len(listX) - count)
        else:
            return (len(listY) - count)
    """
