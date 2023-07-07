def solver(answer,k, s):
    if len(answer)==1:
        return 1
    left, right = 0,1
    nF = 0 if answer[0]!=s else 1
    goal = 0
    while True:
        if right-left > goal:
            goal = right-left
        if right==len(answer):
            return  goal
        if answer[right]==s:
            nF=nF+1
        while nF>k:
            if answer[left]==s:
                nF = nF -1
                left = left + 1
                break
            left = left + 1
        right = right + 1


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tvalue = solver(answerKey, k, 'T')
        print('--')
        fvalue = solver(answerKey, k, 'F')
        return max(tvalue, fvalue)