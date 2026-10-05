class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxLen = 0
        # topFreq = 0
        for r in range(len(s)):
            count[s[r]] += 1
            # windowLen = r - l + 1 
            # cannot pre-define windowLen, must be in the while 
            # loop condition, because it changes and must be 
            # dynamically checked. 
            # topFreq = max(topFreq, count[s[r]])
            while (r-l+1) - max(count.values()) > k and l < r:
                count[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
        