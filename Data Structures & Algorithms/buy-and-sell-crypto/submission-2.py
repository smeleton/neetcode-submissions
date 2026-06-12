class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Brute Force:
        # maxProfit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        # return maxProfit

        ## two pointers/sliding window
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                tempProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, tempProfit)
            else:
                l = r 
        return maxProfit 




        