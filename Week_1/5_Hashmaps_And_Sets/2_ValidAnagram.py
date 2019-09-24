class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #checks if both words have the same length
        if(len(s) - len(t) == 0):
        
            l1 = list(s)
            l2 = list(t)
            
            l1.sort()
            l2.sort()
            
            st1 = ''.join(l1)
            st2 = ''.join(l2)
            
            return st1 == st2
            
        else:
            return False
    
     
