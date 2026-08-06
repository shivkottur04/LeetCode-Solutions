class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        lst=list(s)
        for i in range(len(lst)):
            if lst[i] in d.keys() and d[lst[i]]==1:
                return i
        return -1





        