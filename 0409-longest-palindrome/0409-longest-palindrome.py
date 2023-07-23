class Solution:
    def longestPalindrome(self, s: str) -> int:
        answer = 0
        hasOdd = False
        sCounter = Counter(s)
        for char in sCounter:
            if sCounter[char] % 2 == 0:
                answer += sCounter[char]
            else:
                hasOdd = True
                answer += (sCounter[char] - 1)
        return answer + 1 if hasOdd else answer
        