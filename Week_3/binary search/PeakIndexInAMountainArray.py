class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
       
        #return index of peak
        
        #binary search
        start = 0
        end = len(A)-1
        
        
        while start <= end:
            
            #index of pivot
            pivot = int((start + end)/2)
            
            #if peak return peak index
            if A[pivot] > A[pivot + 1] and A[pivot] > A[pivot - 1]:
                return pivot
            
            else:
                if A[pivot] < A[pivot +1]:
                    start = pivot + 1 
                else: 
                    end = pivot - 1
    
