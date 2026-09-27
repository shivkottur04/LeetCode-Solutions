class Solution:
    def countDigits(self, num: int) -> int:
        lst=list(str(num))
        count=0
        for i in lst:
            if num%int(i)==0:
                count+=1
        return count
        