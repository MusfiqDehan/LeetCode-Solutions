class Solution:
    def isValid(self, s: str) -> bool:
        a_stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in mapping.values():
                a_stack.append(char)
            elif char in mapping.keys():
                if a_stack == [] or mapping[char] != a_stack.pop():
                    return False
            else:
                return False
            
        return a_stack == []
        