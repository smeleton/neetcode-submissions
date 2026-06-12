class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l = 0
        # r = len(heights) - 1
        # maxArea = 0
        # while l < r:
        #     tempArea = (r - l) * min(heights[l], heights[r])
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                tempArea = (j - i) * min(heights[i], heights[j])
                if tempArea > maxArea:
                    maxArea = tempArea
        return maxArea


            
            


        