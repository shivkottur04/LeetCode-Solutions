import numpy as np
class Solution:
    def reverseBits(self, n: int) -> int:
        binary=np.binary_repr(n,width=32)
        
        new=binary[::-1]
        number=int(new,2)
        return number
        