class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        i=0
        while i<len(nums) and sum(nums[i:])!=0:
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            else:
                i+=1
        return nums

        
        