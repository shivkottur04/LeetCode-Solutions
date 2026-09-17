class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n=int(len(arr)*0.25)
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key in d.keys():
            if d[key]>n:
                return key
        return None
