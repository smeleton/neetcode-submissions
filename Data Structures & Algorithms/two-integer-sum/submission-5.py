class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []
        hashtable = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashtable:
                return [hashtable[diff], i]
            hashtable[num] = i