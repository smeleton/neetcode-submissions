class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #naive solution

        #frequency counting
        

        # sliding window technique
        l, r= 0, 0
        hm = defaultdict(int)
        res = 0
        while r < len(s):
            hm[s[r]] += 1
            if (r - l + 1) - max(hm.values()) > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res

        # count = defaultdict(int)
        # res = 0
        # l = 0
        # for r in range(len(s)):
        #     count[s[r]] += 1
        #     if (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)
        # return res



