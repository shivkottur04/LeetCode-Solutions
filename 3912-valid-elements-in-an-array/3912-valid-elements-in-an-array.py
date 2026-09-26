class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        lst=[]
        if len(nums)==1:
            return nums
        for i in range(len(nums)):
            if i==0:
                lst.append(nums[i])
            elif i==len(nums)-1:
                lst.append(nums[i])
            else:
                if nums[i]>max(nums[i+1:]) or nums[i]>max(nums[i-1::-1]) :
                    lst.append(nums[i])
        return lst

