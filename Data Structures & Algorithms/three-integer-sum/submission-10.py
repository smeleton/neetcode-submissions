class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # #naive solution
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(triplet))
        # return [list(i) for i in res]

        #expected approach
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = -nums[i]
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res



        
        