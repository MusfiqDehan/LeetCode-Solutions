class Solution:
	def maxValue(self, n: int, index: int, maxSum: int) -> int:
		maxSum = maxSum - n

		def Helper(value):
			left_max = max(0, value - index)
			result = (value + left_max) * (value - left_max + 1) // 2
			left_max = max(0, value - ((n-1) - index))
			result = result + (value + left_max ) * (value - left_max + 1) // 2
			return (result - value)

		low , high = 0, maxSum

		while low < high:
			mid = (low + high + 1) // 2
			if Helper(mid) <= maxSum:
				low = mid
			else:
				high = mid - 1

		return low + 1
        