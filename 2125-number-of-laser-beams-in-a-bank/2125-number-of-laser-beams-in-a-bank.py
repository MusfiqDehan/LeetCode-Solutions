class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        answer = 0
        prev = 0
        for row in bank:
            curr = row.count('1')
            if curr == 0:
                continue
            answer += curr * prev
            prev = curr
        return answer
