class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)
        for i, c in zip(indices, s):
            result[i] = c
        return "".join(result)