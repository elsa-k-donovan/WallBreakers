class Solution:
    def isHappy(self, n: int) -> bool:
        
        """
        Algorithm runs quickly but it could be re-written to use less 
        memory than it does now.
        """
        
        result = n
    
        """
        use hash set "numbers" to keep track of numbers 
        and whether the result has already been used
        in order to break out of endless loops
        """
        
        numbers = set()
    
        #put separate digits as list elements
        while (result > 1):
            y = 0
            strN = str(result)
            listN = list(strN)
            print(listN)
            
            for x in listN:
                x = int(x)
                a = x*x
                y += a
            
            result = y
            for z in numbers:
                if result == z:
                    return False
                
            numbers.add(result)
            print(result)
            
            
        if result == 1:
            return True
 
        
        
        
