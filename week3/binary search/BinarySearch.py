class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #if target exists return index, otherwise -1
        start = 0
        end = len(nums) - 1
        
        
        while start <= end:
            
            #pivot inside while loop so that it is recalculated
            pivot = int((start + end)/2)
            
            if target == (nums[pivot]):
                return pivot
            else:
                if target > nums[pivot]:
               
                    start = pivot + 1
                else:
                
                    end = pivot - 1
    
        return -1
                
