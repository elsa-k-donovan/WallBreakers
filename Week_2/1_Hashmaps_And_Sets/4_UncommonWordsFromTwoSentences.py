import collections

"""
Used help from Slack for this one.
"""


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        setA = set(A.split())
        setB = set(B.split())
        
        
        wordCounter = collections.Counter(A.split()) + collections.Counter(B.split())
        
        return [k for k, v in wordCounter.items() if v == 1]
        
