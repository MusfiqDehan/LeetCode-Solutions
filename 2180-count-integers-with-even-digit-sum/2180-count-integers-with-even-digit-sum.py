class Solution:
    def countEven(self, num: int) -> int:
	    return sum(sum(int(x) for x in str(i)) % 2 == 0 for i in range(2, num + 1))
        