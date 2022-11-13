class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split()             # ["the", "sky", "is", "blue"]
        rev_s = list(reversed(split_s)) # ["blue", "is", "the", "sky"]
        return " ".join(rev_s)          # "blue is sky the"
        