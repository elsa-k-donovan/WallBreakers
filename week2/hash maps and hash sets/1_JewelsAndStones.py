class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
      #use collections.counter
        countS = collections.Counter(S) #initializing
        listJ = list(J)
        
        jewels = 0
        
        for item in listJ:
            jewels += countS[item]
            
        
        return jewels
