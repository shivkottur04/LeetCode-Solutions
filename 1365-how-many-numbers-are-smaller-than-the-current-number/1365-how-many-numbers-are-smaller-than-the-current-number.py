class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[j]<nums[i]:
                    count[i]+=1
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    count[i]+=1
        return count
                     