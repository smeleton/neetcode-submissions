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

        #Brute Force Time: O(n^2) Space: O()
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


        
        

        