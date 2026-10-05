class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #naive solution:
        s1sorted = sorted(s1)
        m = len(s1)
        for i in range(len(s2) - m + 1):
            if sorted(s2[i:i+m]) == s1sorted:
                return True
        return False

        # if len(s1) > len(s2):
        #     return False
        # windowLen = len(s1)
        # permu = {}
        # tation = defaultdict(int)
        # for i in range(windowLen):
        #     permu[s1[i]] = 1 + permu.get(s1[i], 0)
        #     tation[s2[i]] += 1 
        # if permu == tation: 
        #     return True
        # l = 0    
        # for r in range(windowLen, len(s2)):
        #     tation[s2[r]] += 1 
        #     tation[s2[l]] -= 1
        #     if tation[s2[l]] == 0:
        #         tation.pop(s2[l]) 
        #     l += 1
        #     if permu == tation:
        #         return True
        # return False
        
        # time complexity: O(m + n) -> O(n) n is len(s2) 
        # space complexity: O(26) constant, there could only be 26 characters

        
            
            






        