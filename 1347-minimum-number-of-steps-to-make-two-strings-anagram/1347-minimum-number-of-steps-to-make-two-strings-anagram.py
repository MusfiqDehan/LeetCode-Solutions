class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        for i in set(s):
            s_dict[i] = s.count(i)
        result_change = 0
        for i in s_dict.keys():
            diff = s_dict[i] - t.count(i)
            if diff > 0:
                result_change += diff
        return result_change
