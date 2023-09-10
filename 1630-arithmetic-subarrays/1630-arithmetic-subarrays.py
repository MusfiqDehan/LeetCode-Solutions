class Solution:
    def get_answer(self, diff: int, subquery: List[int]) -> bool:
        for i in range(1, len(subquery) - 1):
            if subquery[i + 1] - subquery[i] != diff:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answers = []
        for start, end in zip(l, r):
            subquery = nums[start:end + 1]
            subquery.sort()
            diff = subquery[1] - subquery[0]
            answers.append(self.get_answer(diff, subquery))
        return answers
        