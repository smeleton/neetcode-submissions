class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort then compare not really a likeable solution, will not pass
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        #time complexity: O(nlogn + mlogm) sorting algorithm 
        #space complexity: O(n+m) 

        #better optimal solution with hash dictionary
        # from collections import defaultdict
        if len(s) != len(t):
            return False
        
        lookupS = defaultdict(int)
        lookupT = defaultdict(int)
        for i in range(len(s)):
            lookupS[s[i]] += 1
            lookupT[t[i]] += 1
        return lookupS == lookupT

        
        