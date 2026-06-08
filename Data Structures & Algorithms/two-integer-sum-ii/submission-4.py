class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Brute force time: O(n^2) Space: O(n)
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        l = 0 
        r = len(numbers) - 1
        while l < r:
            while numbers[l] + numbers[r] > target:
                r -= 1
            while numbers[l] + numbers[r] < target:
                l += 1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]

                    
                
        