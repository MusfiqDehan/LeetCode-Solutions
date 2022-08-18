class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)        
        max_salary = max(salary)
        len_counted = len(salary) - 2
        total_salary = sum(salary)
        remaining_salary = total_salary - (min_salary + max_salary)
        avg_salary = remaining_salary / len_counted
        return avg_salary

        
        