class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst=list(str(n))
        Sum=0
        prod=1
        for i in lst:
            Sum+=int(i)
            prod*=int(i)
        return prod-Sum
            
        