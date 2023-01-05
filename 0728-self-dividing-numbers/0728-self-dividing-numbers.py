class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left,right+1):
            val = i
            res = True
            if "0" not in str(i):
                while val != 0:
                    val1 = val % 10
                    if i%val1!=0:
                        res = False
                    val = val // 10
                if res: ans.append(i)
        return ans
        