class Solution:
    def alternateDigitSum(self, n: int) -> int:
        lst=list(str(n))
        val=0
        for i in range(len(lst)):
            if i%2==0:
                val+=int(lst[i])
            else:
                val-=int(lst[i])
        return val
