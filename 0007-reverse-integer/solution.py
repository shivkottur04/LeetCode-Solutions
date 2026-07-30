class Solution:
    def reverse(self, x: int) -> int:
        original=x
        if x<0:
            x=-x
        x=str(x)
        rev=x[::-1]
        rev=int(rev)
        if rev< -(2)**31  or rev > 2**31-1:
            return 0
        if original<0:
            return -rev
        else:
            return rev
        
