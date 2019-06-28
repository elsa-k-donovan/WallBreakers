class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
      
      #  Still has a runtime error 
        row = []
       
        for x in range(0, len(A)):
            row.append([])
            for i in A:
              row[x].append(i[x])
            
        
        return row
        
