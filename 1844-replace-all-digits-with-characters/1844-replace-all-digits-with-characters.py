class Solution:
    def replaceDigits(self, s: str) -> str:
        replaced_string = ""

        for i in range(0, len(s)):
            if s[i].isnumeric():
                replaced_string += chr(ord(s[i-1])+int(s[i]))
            else:
                replaced_string += s[i]
                
        return replaced_string
        