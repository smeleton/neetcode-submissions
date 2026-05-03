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

        #Method 2: Prefix and Suffix (Optimal)
        # result = [1] * len(nums)
        # prefix = 1
        # for i in range(len(nums)):
        #     result[i] = prefix 
        #     prefix *= nums[i]
        # suffix = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     result[i] *= suffix 
        #     suffix *= nums[i]
        # return result

        #Method 3: prefix and suffix (2 arrays)
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n

        prefix[0] = suffix[n-1] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result


