class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        #first reverse each row
        #then invert
             
            for i in A:
                i.reverse()
                for x in range(0, len(A)):
                    if i[x] == 0:
                        i[x] = 1
                    else:
                        i[x] = 0
                                    
            return A  
