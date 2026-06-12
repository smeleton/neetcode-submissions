class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Brute Force:
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        # return maxProfit

        ## two pointers/sliding window Time: O(n) Space: O(1)
        # l, r = 0, 1
        # maxP = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         maxP = max(maxP, prices[r] - prices[l])
        #     else:
        #         l = r
        #     r += 1
        # return maxP

        ## Dynamic Programming Time: O(n) Space: O(1)
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            minBuy = min(minBuy, sell)
            maxP = max(maxP, sell - minBuy)
        return maxP




        