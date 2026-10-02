class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        currP = 0
        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            currP = max(currP, prices[r] - prices[l])
        return currP
            

        