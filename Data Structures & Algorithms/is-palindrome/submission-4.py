class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filteredS = ''.join(char for char in s if char.isalnum())
        # middle = 
        # for i in range(middle):
        #     if filteredS[i] != filteredS[len(filteredS)-1-i]:
        #         return False
        # return True
        processedS = ''.join(char for char in s if char.isalnum()).lower()
        rS = processedS[::-1]
        return rS == processedS