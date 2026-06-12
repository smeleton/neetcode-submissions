class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            tempArea = (r - l) * min(heights[l], heights[r])
            if tempArea > maxArea:
                maxArea = tempArea
            if heights[l]  < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea

        ## Brute Force Time: O(n^2) Space: O(1)
        # maxArea = 0
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         tempArea = (j - i) * min(heights[i], heights[j])
        #         if tempArea > maxArea:
        #             maxArea = tempArea
        # return maxArea


            
            


        