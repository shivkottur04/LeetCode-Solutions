import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        x=math.log(n,4)
        
        if x==int(x):
            return True
        else:
            return False
        