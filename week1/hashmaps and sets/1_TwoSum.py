class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using an algorithm that calculates backwards to find result.
        Need to start with index as opposed to element within list, 
        which I had been using before.
        """
  
        for i in range(len(nums)):
        
            for j in range(i+1, len(nums)):
                
                if nums[j] == target - nums[i]:
                    return [i,j]
      
                
        
    
            
