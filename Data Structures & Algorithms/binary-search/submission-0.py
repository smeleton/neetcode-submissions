class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #brute force solution
        #linear search 
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1
        # mid = len(nums) // 2
        # if nums[i] == target:
        #     return i
        # elif nums[i] < target:
        #     search(nums[mid:], target)
        # elif nums[i] > target:
        #     search(nums[:mid], target)
        

                
        