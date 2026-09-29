class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #return list of lists [[], [], [], ...]
        output = defaultdict(list)
        for i in range(len(strs)):
            sortedStr = str(sorted(strs[i]))
            output[sortedStr].append(strs[i])
        return list(output.values())
