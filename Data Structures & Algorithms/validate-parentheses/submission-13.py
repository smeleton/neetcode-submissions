class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {')':'(', '}':'{',']':'['}
        for char in s:
            if char in hm:
                if stack and stack[-1] == hm[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack



        