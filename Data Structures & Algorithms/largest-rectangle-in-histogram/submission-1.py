class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        stack = [] #pair (index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                poppedInd, poppedH = stack.pop()
                maxArea = max(maxArea, poppedH * (i - poppedInd))
                start = poppedInd
            stack.append((start, h))
        
        while stack:
            ind, h = stack.pop()
            maxArea = max(maxArea, h * (len(heights) - ind))
        return maxArea
            

        