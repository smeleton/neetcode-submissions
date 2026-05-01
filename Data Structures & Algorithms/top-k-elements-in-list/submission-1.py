class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. The intuitive method:
        #Thought process: find frequency of each number -> sort by frequency -> take top k
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1 
        
        # freq =[]
        # for n, c in count.items():
        #     freq.append([c, n])
        # freq.sort()

        # res = []
        # while len(res) < k:
        #     res.append(freq.pop()[1])
        # return res
        
        #Efficient bucket sort method 
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



                