class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        # create a new array B
        # for loop to read through array
        # if-else
        
        arrayB = []
        
        for i in A:
            if A[i] % 2 == 0:
                arrayB.insert(0,i)
            else:
                arrayB.append(i)
    
        return arrayB
        
