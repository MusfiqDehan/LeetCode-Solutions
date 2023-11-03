class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target_len = len(target)
        prev = 0
        for i in range(0,target_len):
            res += (['Push', 'Pop'])*(target[i] - prev - 1) + ['Push']
            prev = target[i]
        return res
        