class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num2 = [str(i) for i in num]
        str2 = "".join(num2)
        num_str = int(str2)
        res = num_str + k
        res_str = str(res)
        res2 = [int(j) for j in res_str]
        return res2