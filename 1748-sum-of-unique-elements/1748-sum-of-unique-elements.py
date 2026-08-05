class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sum=0
        for key,value in d.items():
            if value==1:
                sum+=key
        
        return sum
        