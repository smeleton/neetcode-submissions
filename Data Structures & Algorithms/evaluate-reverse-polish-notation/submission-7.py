class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {'+':operator.add, 
                     '-':operator.sub, 
                     '*':operator.mul, 
                     '/':operator.truediv}
        stack = []
        for char in tokens:
            if char in operators:
                roperand = stack.pop()
                loperand = stack.pop()
                stack.append(
                    int(operators[char](loperand, roperand)))
            else:
                stack.append(int(char))
        return stack[-1]
        
        