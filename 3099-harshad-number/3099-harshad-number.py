class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        lst=list(str(x))
        lst=list(map(int,lst))
        return sum(lst) if x%sum(lst)==0 else -1
        