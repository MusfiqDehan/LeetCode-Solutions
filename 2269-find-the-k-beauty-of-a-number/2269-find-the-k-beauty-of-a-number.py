class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        i = 0
        j = k
        count = 0
        while j <= len(str(num)):
            piece = str(num)[i:j]
            if int(piece) > 0 and num % int(piece) == 0: count += 1
            i += 1
            j += 1
        return count