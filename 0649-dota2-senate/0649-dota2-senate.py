class Solution:
    def predictPartyVictory(self, senate: str) -> str:       
        ref = {"D": "Dire", "R":"Radiant"}
        res = senate
        stack = []
        while len(set(res)) == 2:
            res_cur = []
            for i in res:
                if not stack or stack[-1] == i:
                    stack.append(i)
                    res_cur.append(i)
                elif stack[-1] != i:
                    stack.pop()
            res = res_cur
        if stack:
            return ref[stack[0]]
        return ref[senate[0]]
        