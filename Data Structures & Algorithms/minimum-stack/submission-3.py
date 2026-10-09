class MinStack:
    # two stack solution 
    # def __init__(self):
    #     self.stack = []
    #     self.minStack = []
        
    
    # def push(self, val: int) -> None:
        
    #     self.stack.append(val)
    #     if self.minStack:
    #         val = min(val, self.minStack[-1])
    #     self.minStack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.minStack.pop()
        
    # def top(self) -> int:
    #     return self.stack[-1]
    
    # def getMin(self) -> int:
    #     return self.minStack[-1]
    
    # one stack tuple solution:

    def __init__(self):
        self.stack = []        

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))
    
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[-1][0]
    
    def getMin(self):
        return self.stack[-1][1]

        
