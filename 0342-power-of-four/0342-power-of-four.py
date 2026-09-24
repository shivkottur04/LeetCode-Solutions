import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        x=math.log(n,4)
        y=int(x)
        if x==y:
            return True
        else:
            return False
        