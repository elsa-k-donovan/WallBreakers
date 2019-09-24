class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 0:
            return False
        else:
            total = 1
            while total < n:
                total *= 2
    
        return total == n
