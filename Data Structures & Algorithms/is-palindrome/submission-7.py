class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## 1. brute force reverse the string
        # processedS = ''.join(char for char in s if char.isalnum()).lower()
        # return processedS == processedS[::-1]
        ## time complexity: O(n)
        ## space complexity: O(n)

        # 2. optimal solution
        # 2 pointer string length implementation
        # processedS = ''.join(char for char in s if char.isalnum()).lower()
        # middle = len(processedS) // 2
        # for i in range(middle):
        #     if processedS[i] != processedS[len(processedS)-1-i]:
        #         return False
        # return True
        # time complexity: O(n)
        # space complexity: O(1)

        # 2 pointer more general implementation without building a new string
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
        
