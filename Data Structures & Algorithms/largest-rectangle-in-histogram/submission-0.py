class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = []
        for i, h in enumerate(heights):
            poppedInd = i
            while stack and h < stack[-1][1]:
                poppedInd, poppedH = stack.pop()
                maxArea = max(maxArea, poppedH * (i - poppedInd))
            stack.append([poppedInd, h])
        
        while stack:
            ind, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - ind))
        return maxArea
            

        