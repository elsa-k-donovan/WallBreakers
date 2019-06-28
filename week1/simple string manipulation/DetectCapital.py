class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        #All uppercase condition
        if word.isupper():
            return True
        
        #All lowercase condition
        elif word.islower():
            return True
        
        #First letter capital
        elif word[0].isupper():
            
            #Remove First char from word using Slice
            if word[1:].islower():
                return True
            else:
                return False
        
        else:
            return False
