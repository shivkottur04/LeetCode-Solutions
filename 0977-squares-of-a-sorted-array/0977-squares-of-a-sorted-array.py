class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i]*=nums[i]
        lst=[]
        i=0
        n=len(nums)
        while i<n:
            x=min(nums)
            nums.remove(x)
            lst.append(x)
            i+=1
        return lst
        
        