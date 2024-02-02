class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        q = deque([num for num in range(1,10)])
        ans = []
        while q:
            num = q.popleft()
            if num > high:
                return ans
            if low <= num <= high:
                ans.append(num)
            last = num % 10
            if last < 9:
                q.append(num * 10 + last + 1)
        return ans       
        