class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        new_s = [i[::-1] for i in s]
        return " ".join(new_s)
        