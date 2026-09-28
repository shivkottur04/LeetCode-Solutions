class Solution:
    def digitCount(self, num: str) -> bool:
        num=list(num)
        for i in range(len(num)):
            if int(num[i])!=num.count(str(i)):
                return False
        return True

        