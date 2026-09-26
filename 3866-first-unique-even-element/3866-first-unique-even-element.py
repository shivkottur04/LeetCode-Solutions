class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i%2==0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        for key in d.keys():
            if d[key]==1:
                return key
        return -1