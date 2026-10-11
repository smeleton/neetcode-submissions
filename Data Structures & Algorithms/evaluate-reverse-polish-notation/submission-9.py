class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        operators = {'+':operator.add, 
                     '-':operator.sub, 
                     '*':operator.mul, 
                     '/':operator.truediv}
        stack = []
        for token in tokens:
            if token in operators:
                roperand = stack.pop()
                loperand = stack.pop()
                stack.append(
                    int(operators[token](loperand, roperand)))
            else:
                stack.append(int(token))
        return stack[-1]
        
        