class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        lst=[]
        for key in d.keys():
            if d[key]>len(nums)/3:
                lst.append(key)
        return lst