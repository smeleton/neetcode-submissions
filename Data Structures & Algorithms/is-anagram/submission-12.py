class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort then compare not really a likeable solution, will not pass
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        #time complexity: O(nlogn) sorting algorithm 
        #space complexity: O(n)

        #better optimal solution with hash dictionary
        # from collections import defaultdict
        # lookupS = defaultdict(int)
        # lookupT = defaultdict(int)
        # for char in s:
        #     lookupS[char] += 1
        # for char in t:
        #     lookupT[char] += 1
        # return lookupS == lookupT

        
        