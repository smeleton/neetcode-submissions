class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #return list of lists [[], [], [], ...]
        # #brute force/naive solution 
        # output = defaultdict(list)
        # for i in range(len(strs)):
        #     sortedStr = str(sorted(strs[i])) #sort each string O(nlogn)
        #     output[sortedStr].append(strs[i])
        # return list(output.values())
        # #time complexity: O(m*nlogn) m = number of strings, n = length of the longest str
        # #space complexity: O(m) 

        #creative & optimal solution
        #create a alphabet lookup table(dictionary) 
        # lookup = {chr(ord('a') + i): 0 for i in range(26)}
        match = defaultdict(list)
        for str in strs:
            lookup = [0] * 26
            for char in str:
                lookup[ord(char) - ord('a')] += 1
            match[tuple(lookup)].append(str)
        return list(match.values())
            





