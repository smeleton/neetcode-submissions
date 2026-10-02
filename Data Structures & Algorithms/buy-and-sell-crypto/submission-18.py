class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #naive solution
        # double for loop, check every possible buy-sell pair
        currP = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                currP = max(currP, prices[j] - prices[i])
        return currP
        # time complexity: O(n^2)
        # space complexity: O(1)
                
        # optimal/expected solution
        # dynamic sliding window
        # l = 0
        # currP = 0
        # for r in range(len(prices)):
        #     while prices[l] > prices[r]:
        #         l = r
        #     currP = max(currP, prices[r] - prices[l])
        # return currP
        # time complexity: O(n)
        # space complexity: O(1)

            

        