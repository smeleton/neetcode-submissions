#define doubly linked list class 
class DoublyLL:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        head = DoublyLL(tokens[0])
        curr = head

        # creating and linking nodes
        for i in range(1, len(tokens)):
            curr.next = DoublyLL(tokens[i], prev=curr, next=None)
            curr = curr.next
        
        while head is not None:
            if head.val in '+-*/':
                l = int(head.prev.prev.val)
                r = int(head.prev.val)
                match head.val:
                    case '+':
                        res = l + r
                    case '-':
                        res = l - r 
                    case '*':
                        res = l * r
                    case '/':
                        res = int(l / r)
                head.val = str(res)
                head.prev = head.prev.prev.prev
                if head.prev is not None:
                    head.prev.next = head
            
            ans = int(head.val)
            head = head.next
        return ans

                    

        
        
        
        
        

        