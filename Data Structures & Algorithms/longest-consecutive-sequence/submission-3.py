class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Efficient Method Time: O(n) Space: O(n)
        # numSet = set(nums)
        # longest = 0
        # for n in nums:
        #     if (n - 1) not in numSet:
        #         length = 0
        #         while (n + length) in numSet:
        #             length += 1
        #         longest = max(longest, length)
        # return longest

        #Brute Force Time: O(n^2) Space: O(n)
        numSet = set(nums)
        longest = 0
        for num in nums:
            length = 0
            curr = num 
            while curr in numSet:
                length += 1
                curr += 1
            longest = max(length, longest)
        return longest

        ## Sorting Method Time: O(nlogn) Space: O(n)
        sortedList = sorted(nums)
        longest = 0
        curr = nums[0]
        length = 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                length = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            length += 1
            curr += 1
            longest = max(longest, length)
        return longest
            

        
        

        