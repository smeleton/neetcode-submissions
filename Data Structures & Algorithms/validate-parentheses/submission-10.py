# class Solution:
#     def isValid(self, s: str) -> bool:
        # hm = {'}' : '{', ')' : '(', ']' : '['}
        # openStack = []
        # for char in s:
        #     if char in hm:
        #         if openStack and openStack[-1] == hm[char]:
        #             openStack.pop()
        #         else:
        #             return False
        #     else:
        #         openStack.append(char)
        # return not openStack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        