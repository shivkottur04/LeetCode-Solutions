class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=dict(sorted(d.items(),key=lambda x:(x[1],-x[0]),reverse=False))
        lst=[]
        for key in d.keys():
            lst.extend([key]*d[key])
        return lst