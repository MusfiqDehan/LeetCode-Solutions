class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        return all(x == arr[0] + i*diff for i,x in enumerate(arr))