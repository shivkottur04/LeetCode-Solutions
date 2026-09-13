class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d={}
        a=s1.split()
        b=s2.split()
        for i in a:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in b:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        lst=[]
        for key in d.keys():
            if d[key]==1:
                lst.append(key)
        return lst