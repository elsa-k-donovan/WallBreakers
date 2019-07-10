class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        i = 0
        j = 0
        
        #puts in order lowest to highest
        #s = size of cookie
        g.sort()
        s.sort()
        
        while i < len(g) and j < len(s):
            #only count when size of cookie is greater than greed
            #if result is found move to next child(greed)
            if s[j] >= g[i]: 
                result += 1
                i +=1
            j +=1
        
        return result
            
