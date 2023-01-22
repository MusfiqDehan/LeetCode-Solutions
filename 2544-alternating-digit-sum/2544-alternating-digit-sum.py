class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        total = int(n[0])
        prev_sign = 1
        for i in range(1, len(n)):
            if prev_sign == 1:
                total += int(n[i]) * -1
                prev_sign = -1
            else:
                total += int(n[i])
                prev_sign = 1
        return total

        