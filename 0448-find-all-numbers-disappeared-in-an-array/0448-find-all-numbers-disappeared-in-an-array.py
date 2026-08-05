class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d={}
        lst=[]
        for i in range(1,len(nums)+1):
            d[i]=1
        for i in nums:
            d[i]+=1
        for key in d.keys():
            if d[key]==1:
                lst.append(key)

        return lst

