class Solution(object):
    def findTheDifference(self, s, t):
        d={}
        lst=[]
        for i in t:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in s:
            if i in d.keys():
                d[i]-=1
        for key,val in d.items():
            if val>0:
                lst.append(key)
        return "".join(lst)
        
        

    
        