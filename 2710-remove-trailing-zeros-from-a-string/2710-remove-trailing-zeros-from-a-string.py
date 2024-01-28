class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        if num[-1] != '0':
            return num
        return self.removeTrailingZeros(num[:-1])