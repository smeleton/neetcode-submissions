class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## 1. brute force reverse the string
        # processedS = ''.join(char for char in s if char.isalnum()).lower()
        # return processedS == processedS[::-1]
        ## time complexity: O(n)
        ## space complexity: O(n)

        # 2. optimal solution - 2 pointers I think?
        processedS = ''.join(char for char in s if char.isalnum()).lower()
        middle = len(processedS) // 2
        for i in range(middle):
            if processedS[i] != processedS[len(processedS)-1-i]:
                return False
        return True
        # time complexity: O(n)
        # space complexity: O(1)
