class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(c**0.5)
        while i<=j:
            val=i**2+j**2
            if val==c:
                return True
            elif val<c:
                i+=1
            else:
                j-=1
        return False