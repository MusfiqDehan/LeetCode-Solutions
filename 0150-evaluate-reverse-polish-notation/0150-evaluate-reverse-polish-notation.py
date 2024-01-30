class Solution(object):
    def evalRPN(self, tokens):
        
        stack = []

        operator = set("+-*/")

        for token in tokens:

            if token not in operator:
                stack.append( int(token) )
                continue

            second, first= stack.pop(), stack.pop()

            if token == "+":
                result = first + second
            elif token == "-":
                result = first - second
            elif token == "*":
                result = first * second
            else:
                result = int(first / second)

            stack.append(result)

        return stack.pop()
        