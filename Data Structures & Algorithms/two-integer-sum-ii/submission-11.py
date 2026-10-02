class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Optimal solution
        # # two pointer, one at the begin, one at the end
        # l, r = 0, len(numbers) - 1
        # while l < r:
        #     if numbers[l] + numbers[r] < target:
        #         l += 1
        #     elif numbers[l] + numbers[r] > target:
        #         r -= 1 
        #     else:
        #         return [l+1, r+1]
        # # time complexity: O(n)
        # # space complexity: O(1)

        #hashmap solution
        hashmap = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in hashmap:
                return [hashmap[diff], i+1]
            hashmap[numbers[i]] = i+1
        return []
        
        # #naive solution
        # for i in range(len(numbers)):
        #     for j in range(i, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        # # time complexity: O(n^2) double for loop 
        # # space complexityL O(1)
        