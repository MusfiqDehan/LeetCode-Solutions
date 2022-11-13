class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()
        rev_s = list(reversed(split_s))
        return " ".join(rev_s)
        