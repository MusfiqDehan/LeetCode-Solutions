class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for item in pushed:
            # push element to the stack
            stack.append(item)
            # unless the stack is empty
            while len(stack) > 0 and stack[-1] == popped[i]:
                # if last element of stack equal to popped element 
                stack.pop()
                # we are incrementing i
                i += 1
        return len(stack) == 0