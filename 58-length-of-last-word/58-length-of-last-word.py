class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_s = s.split()
        # len_split_s = len(split_s)
        last_word = split_s[-1]
        len_last_word = len(last_word)
        return len_last_word
        