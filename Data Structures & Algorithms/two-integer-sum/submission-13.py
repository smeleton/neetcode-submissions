class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        #time complexity: O(n^2) double for loop
        #space complexity: O(1) does not create any new data structures

        #optimal solution / one single pass
        heap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in heap:
                return [heap[diff], i]
            diff[nums[i]] = i




        
        