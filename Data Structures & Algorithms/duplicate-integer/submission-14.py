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
        # 1. convert list to set then check for length / not practical

        # s = set(nums)
        # return len(s) != len(nums)
        #time complextiy: O(n) depends on the set function? 
        #space complexity: O(n) constructs a set roughly the same length as nums

        #2a. hashing with set
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False
        #time complexity: O(n) one forward pass
        #spcae complexity: O(n) constructs a set

        #2b. hashing with dictionary
        seen = {}
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 0
        return False

        #3. sorting
        # sl = sorted(nums)
        # for i in range(1, len(sl)):
        #     if sl[i] == sl[i-1]:
        #         return True
        # return False
        #time complexity: O(n*logn) from the sorting
        #space compextiy: O(n) or O(1) depending on the sorting algorithm




        
        

        
            