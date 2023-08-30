class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        ans = 0

        for i in points:
            arr.append(i[0])

        arr.sort()

        for i in range(1, len(arr)):
            if (ans < arr[i] - arr[i-1]):
                ans = arr[i] - arr[i-1]
        return ans
