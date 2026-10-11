class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack and if/else (switch) statements solution
        stack = []
        for token in tokens:
            if token in '+-*/':
                roperand = int(stack.pop())
                loperand = int(stack.pop())
                if token == '+':
                    result = loperand + roperand
                elif token == '-':
                    result = loperand - roperand
                elif token == '*':
                    result = loperand * roperand
                elif token == '/':
                    result  = int(loperand / roperand)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]
