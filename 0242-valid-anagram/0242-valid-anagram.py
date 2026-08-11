class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            d1={}
            d2={}
            for i in s:
                if i in d1:
                    d1[i]+=1
                else:
                    d1[i]=1
            for i in t:
                if i in d2:
                    d2[i]+=1
                else:
                    d2[i]=1
            if d1.items()==d2.items():
                return True
            else:
                return False