class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        b="".join(map(str,b))
        b=int(b)
        return pow(a,b,1337)
        