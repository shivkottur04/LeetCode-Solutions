class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
        if d:
            d=dict(sorted(d.items(),key=lambda x:(-x[1],x[0])))
            for key in d.keys():
                return key
        else:
            return -1

        