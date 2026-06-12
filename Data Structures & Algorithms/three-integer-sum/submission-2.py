class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute Force
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))
        # return [list(sum) for sum in res]

        # clever O(n^2) time solution
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
                
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target = 0 - nums[i]
                if nums[l] + nums[r] > target:
                    r -= 1 
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
                    

        
        
                        
        