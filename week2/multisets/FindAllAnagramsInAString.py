class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        """
        Find solution with multiset and without multiset
        """
        
        #compare counts of characters rather than calculating anagrams
        
        #counter of p
        charCount = collections.Counter(p)
        
        #length of p
        length = len(p)
        
        #start string s
        
        
        
        
        print(charCount)
