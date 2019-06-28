class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        #size = len(digits)
        #digits[size-1] += 1
        
        #convert to string then to single int
        total = [str(i) for i in digits] 
        x = int("".join(total))
        x+=1
        
        #convert back to list
        result = (list(str(x)))
        
        #create new empty list for ints
        newList = []
        for y in result:
            newList.append(int(y))
        
        return newList
        
            
