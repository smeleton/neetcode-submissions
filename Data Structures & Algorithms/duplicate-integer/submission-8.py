class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #brute force solution
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        #Runtime exceeds brute force does not work on long input list
        #time complexity: O(n^2)
        #space complexity: O(1)

        #optimal solution:
        # 1. convert list to set then check for length
        # s = set(nums)
        # return len(s) != len(nums)
        #time complextiy: O(1) depends on the set function? 
        #space complexity: O(n) constructs a set roughly the same length as nums

        #2. hashing
        # hash = set()
        # for i in nums:
        #     if i in hash:
        #         return True
        #     hash.add(i)
        # return False
        #time complexity: O(n) one forward pass
        #spcae complexity: O(n) constructs a set

        #sort
        sl = sorted(nums)
        for i in range(len(nums)-1):
            if sl[i] == sl[i+1]:
                return True
        return False



        
        

        
            