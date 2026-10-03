class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #naive solution
        # # use set to track seen characters
        # maxLen = 0
        # for i in range(len(s)):
        #     seen = set()
        #     j = i
        #     while j < len(s) and s[j] not in seen:
        #         seen.add(s[j])
        #         j += 1
        #     maxLen = max(maxLen, j - i)
        # return maxLen
        # # time complexity: O(n^2)
        # # space complexity: O(n)
                
        #expected approach: dynamic sliding window technique
        l = 0
        maxLen = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen

            

        
        