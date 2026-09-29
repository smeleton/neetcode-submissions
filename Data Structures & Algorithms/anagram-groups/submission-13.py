class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #return list of lists [[], [], [], ...]
        # # 1. brute force/naive solution 
        # output = defaultdict(list)
        # for s in strs:
        #     sortedStr = str(sorted(s)) #sort each string O(nlogn)
        #     output[sortedStr].append(s)
        # return list(output.values())
        # #time complexity: O(m*nlogn) m = number of strings, n = length of the longest str
        # #space complexity: O(m) 

        # 2. creative & optimal solution
        # create a alphabet lookup table(dictionary) 
        # lookup = {chr(ord('a') + i): 0 for i in range(26)}
        match = defaultdict(list)
        for s in strs:
            lookup = [0] * 26
            for char in s:
                lookup[ord(char) - ord('a')] += 1
            match[tuple(lookup)].append(s)
        return list(match.values())
            





