class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(max(stones))
            m2 = max(stones)
            stones.remove(max(stones))
            if m1 > m2:
                m1 -= m2
                stones.append(m1)
        if stones:
            return stones[0]
        else:
            return 0
        