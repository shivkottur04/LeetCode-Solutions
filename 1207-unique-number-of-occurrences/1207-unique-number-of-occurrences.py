class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=set(d.values())
        if len(d)==len(s):
            return True
        else:
            return False
        