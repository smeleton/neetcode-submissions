class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Method 1: Brute Force
        # result = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             prod *= nums[j]
        #     result.append(prod)
        # return result

        #Method 2: Prefix and Suffix 
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix 
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix 
            suffix *= nums[i]
        return result

