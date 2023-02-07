class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        n = len(fruits)
        while j < n and fruits[i] == fruits[j]:
            j += 1
        if j == n:
            return n

        l, r = i, j + 1
        answer = 0
        while r < n:
            if fruits[r] != fruits[j]:
                if fruits[r] == fruits[i]:
                    i = j
                    j = r
                else:
                    answer = max(answer, r - l)
                    i = j
                    l = j
                    j = r
            r += 1
        answer = max(answer, r - l)
        return answer
        