class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack and if/else (switch) statements solution

        # #if/elif/else solution
        # stack = []
        # for token in tokens:
        #     if token in '+-*/':
        #         roperand = int(stack.pop())
        #         loperand = int(stack.pop())
        #         if token == '+':
        #             result = loperand + roperand
        #         elif token == '-':
        #             result = loperand - roperand
        #         elif token == '*':
        #             result = loperand * roperand
        #         else:
        #             result  = int(loperand / roperand)
        #         stack.append(result)
        #     else:
        #         stack.append(int(token))
        # return stack[0]
        # #time complexity: O(n)
        # # space complexity: O(n)

        #switch statement 
        stack = []
        for token in tokens:
            if token in '+-*/':
                rop = stack.pop()
                lop = stack.pop()
                match token:
                    case '+':
                        result = lop + rop
                    case '-':
                        result = lop - rop
                    case '*':
                        result = lop * rop
                    case '/':
                        result = int(lop / rop)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
                    
                    

