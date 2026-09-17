class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=dict(sorted(d.items(),key=lambda x:x[0],reverse=True))
        for key in d.keys():
            if d[key]==key:
                return key
        return -1
        