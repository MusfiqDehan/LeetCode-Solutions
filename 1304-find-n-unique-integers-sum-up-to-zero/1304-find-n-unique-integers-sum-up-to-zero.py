class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        counter = 1
        if n % 2 == 0:
            while(len(answer) < n):
                answer.append(counter)
                answer.append(counter * -1)
                counter += 1
        else:
            while(len(answer) < n - 1):
                answer.append(counter)
                answer.append(counter * -1)
                counter += 1
            answer.append(0)

        return answer
        