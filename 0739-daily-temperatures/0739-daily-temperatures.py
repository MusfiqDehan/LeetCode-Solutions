class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)
        #count = 0
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp , j = stack.pop()
                answer[j] = i - j
            stack.append([temperatures[i], i])
        return answer


        