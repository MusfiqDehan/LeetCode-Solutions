class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref_sums = [0] * k
        count = 0
        zero_pos = 0
        for num in nums:
            zero_pos = (zero_pos - num) % k
            pref_sums[(num + zero_pos) % k] += 1
            count += pref_sums[zero_pos]

        return count
        