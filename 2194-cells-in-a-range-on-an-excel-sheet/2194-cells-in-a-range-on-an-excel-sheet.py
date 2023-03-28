class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        # Rows
        r1 = int(s[1])
        r2 = int(s[-1])

        # Columns
        c1 = s[0]
        c2 = s[-2]

        op = []
        for col in range(alpha.index(c1), alpha.index(c2)+1):
            for row in range(r1, r2+1):
                op.append(alpha[col] + str(row))
        return op