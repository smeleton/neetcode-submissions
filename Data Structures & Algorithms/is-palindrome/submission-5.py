class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. brute force reverse the string
        processedS = ''.join(char for char in s if char.isalnum()).lower()
        return processedS == processedS[::-1]



        # processedS = ''.join(char for char in s if char.isalnum()).lower()
        # middle = 
        # for i in range(middle):
        #     if processed[i] != processed[len(processed)-1-i]:
        #         return False
        # return True
