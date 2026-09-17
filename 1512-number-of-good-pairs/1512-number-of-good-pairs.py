class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        lst=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    lst.append((i,j))
        return len(lst)
        