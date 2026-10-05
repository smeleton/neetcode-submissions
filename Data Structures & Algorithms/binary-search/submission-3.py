class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # #brute force solution
        # #linear search 
        # for i, n in enumerate(nums):
        #     if n == target:
        #         return i
        # return -1
        # # time complexity: O(n)
        # # space complexity: O(1)

        # binary search
        # array must be sorted for this to work
        # iterative approach
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return -1


                
        