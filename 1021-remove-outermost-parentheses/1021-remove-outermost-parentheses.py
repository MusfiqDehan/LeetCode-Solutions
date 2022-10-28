class Solution:
    def removeOuterParentheses(self, S):
        stack = []
        opened = 0
        
        for char in S:
            if char == '(' and opened > 0: stack.append(char)
            if char == ')' and opened > 1: stack.append(char)
                
            if char == '(':
                opened += 1 
            else: 
                opened -= 1
            
        return "".join(stack)
        