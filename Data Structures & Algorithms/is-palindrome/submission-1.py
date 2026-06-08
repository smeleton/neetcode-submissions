class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Intuitive solution Time: O(n) Space: O(n)
        # cleaned = "".join(char for char in s if char.isalnum()).lower()
        # for i in range(len(cleaned)):
        #     if cleaned[i] != cleaned[-1 - i]:
        #         return False
        # return True 

        # Clever solution:
        l = 0 
        r = len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and  not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False 
            l += 1
            r -= 1
        return True
            

        