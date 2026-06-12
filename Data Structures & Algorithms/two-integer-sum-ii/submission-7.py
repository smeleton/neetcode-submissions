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
            tempSum = numbers[l] + numbers[r]
            if tempSum > target:
                r -= 1
            elif tempSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        #hash method: requires O(n) space complexity but problem requires O(1)
        # mp = {}
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if diff in mp:
        #         return [mp[diff] + 1, i+1]
        #     mp[numbers[i]] = i
        # return []

                    
                
        