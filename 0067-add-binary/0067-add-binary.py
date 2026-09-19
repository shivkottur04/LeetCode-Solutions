class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=int(a,2)
        b=int(b,2)
        val=a+b
        val=str(bin(val))
        return val[2:]
        