# Time Complexity: O(n^2)
# Due to presence of an 'in' statement within a for-loop, which are both O(n).

class Solution:
    def isValid(self, s: str) -> bool:
        
        openPar = ["{", "[", "("];
        closePar = ["}", "]", ")"];
        
        #implementing stack LIFO from List
        myStack = [];
        
        for elem in s:          #O(n)
            #condition for open parentheses
            if elem in openPar:    #O(n)
                myStack.append(elem);
            
            #condition for closed parentheses
            #only pop from stack if corresponding closed bracket
            elif elem in closePar:   #O(n)
                if (len(myStack) != 0):
                    position = closePar.index(elem);
                    if(myStack[len(myStack)-1] == openPar[position]):
                        print(myStack[len(myStack)-1]);
                        print(openPar[position]);
                        myStack.pop();
                    else:
                        return False;
                else:
                    return False;
            else: 
                return False;
        
        
        if (len(myStack) == 0):
            return True;
