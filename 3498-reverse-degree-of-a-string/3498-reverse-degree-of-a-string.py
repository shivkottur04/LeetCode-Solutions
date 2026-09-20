class Solution:
    def reverseDegree(self, s: str) -> int:
        value=0
        for i in range(len(s)):
            deg=ord(s[i])-ord('a')
            rev_deg=26-deg
            value+=(i+1)*rev_deg
        return value