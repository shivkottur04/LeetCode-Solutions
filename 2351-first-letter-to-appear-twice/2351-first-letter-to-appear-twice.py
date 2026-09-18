class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>1:
                return i
        