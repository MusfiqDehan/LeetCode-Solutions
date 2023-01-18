class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        indexx = 0
        count = 0
        for i in heights:
                if i != expected[indexx]:
                    count += 1
                indexx += 1
        return count