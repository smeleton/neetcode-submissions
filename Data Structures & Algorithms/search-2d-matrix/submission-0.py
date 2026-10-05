class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #brute force solution:
        #every every entry of the matrix 
        for row in matrix:
            for col in row:
                if col == target:
                    return True 
        return False
        