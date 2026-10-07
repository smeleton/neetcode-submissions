class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        
    
        hm = {'}' : '{', ')' : '(', ']' : '['}
        openStack = []
        for char in s:
            if char in hm:
                if openStack and openStack[-1] == hm[char]:
                    openStack.pop()
                else:
                    return False
            else:
                openStack.append(char)
        return not openStack

        