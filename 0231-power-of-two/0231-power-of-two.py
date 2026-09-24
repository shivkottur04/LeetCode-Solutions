import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        x=math.log2(n)
        y=int(x)
        if x==y:
            return True
        else:
            return False

        