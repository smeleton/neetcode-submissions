class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force solution:
        #every every entry of the matrix 
        for row in matrix:
            for col in row:
                if col == target:
                    return True 
        return False
        # time complexity: O(n^2)
        # space complexity: O(1)
        
        #expected approach - binary search

        # expected time complexity: O(log(m * n))
        #binary search template 
        top, bottom = 0, len(matrix) - 1
        theRow = None
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] < target: 
                top = mid + 1
            else:
                if matrix[mid][0] > target:
                    bottom = mid - 1
                else:
                    theRow = matrix[mid]

        l, r = 0, len(theRow) - 1
        while l <= r:
            mid (l + r) // 2
            if theRow[mid] < target:
                l = mid + 1
            elif theRow[mid] > target:
                r = mid - 1
            else:
                return True 
        return False
 