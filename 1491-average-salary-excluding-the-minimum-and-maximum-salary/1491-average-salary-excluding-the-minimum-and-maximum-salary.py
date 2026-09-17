class Solution:
    def average(self, salary: list[int]) -> float:
        minimum=min(salary)
        maximum=max(salary)
        salary.remove(minimum)
        salary.remove(maximum)
        return sum(salary)/len(salary)
        