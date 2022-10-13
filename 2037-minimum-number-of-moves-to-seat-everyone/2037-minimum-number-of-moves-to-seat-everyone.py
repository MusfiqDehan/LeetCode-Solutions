class Solution:
        def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
            return sum(abs(e - t) for e, t in zip(sorted(seats), sorted(students)))
        