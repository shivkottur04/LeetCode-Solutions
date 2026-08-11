class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x=0
        while 3**x<=n:
            if n==3**x:
                return True
            else:
                x+=1
        return False
            