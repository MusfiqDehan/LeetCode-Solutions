class Solution:
    def maxCoins(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        arr=sorted(arr)
        count=0
        while l<r:
            val=([arr[l]]+arr[r-1:r+1])
            print(val)
            count+=val[1]
            l+=1
            r-=2
        return count
        