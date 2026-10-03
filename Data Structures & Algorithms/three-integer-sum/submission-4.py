class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # #brute force solution:
        # # triple for loop - check every possible triplets in the list 
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 triplet = tuple([nums[i], nums[j], nums[k]])
        #                 res.add(triplet)
        # return [list(i) for i in res]
        # # time complexity: O(n^3)
        # # space complexity: O(m)

        # optimal solution
        # two pointer 
        # need to sort the list

        res = set()
        nums.sort() #sort list in place, does not create new list
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    triplet = tuple([nums[i], nums[l], nums[r]])
                    res.add(triplet)
                    l += 1
                    r -= 1
        return [list(x) for x in res]





