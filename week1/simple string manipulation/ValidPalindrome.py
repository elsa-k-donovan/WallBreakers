class Solution:
    def isPalindrome(self, s: str) -> bool:
        
            #remove spaces and non alphanumeric characters
            #check if reverse equals non-reverse
        
         #   tmp = s.replace(" " ,"").replace(",","").replace(":","").replace(".","")
        
        #used a regular expression instead
        
            import re
            s = re.sub('[^0-9a-zA-Z]+', '', s)
            tmp = s
           
        
            #make all lowervcase
            tmp = tmp.lower()
            print(tmp)
                
            reverse = tmp[::-1]
        
        
            if tmp == reverse:
                return True
            else:
                return False
