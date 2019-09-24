class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        """
        Good runtime - but I am working on creating code
        that takes up less memory. Trying to use less variables.
        """
        
        totalCandy = len(candies)
        sisterCandy = int(totalCandy/2)
        
        diffCandy = len(set(candies))

        
        if sisterCandy > diffCandy:
            return diffCandy
        else:
            return sisterCandy
