class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        tempProfit = 0
        maxProfit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l] and l < r:
                l = r
            else:
                tempProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, tempProfit)
        return maxProfit



        