class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i=0
        maximum=nums[0]
        Sum=0
        while i<len(nums):
            Sum=max(nums[i],Sum+nums[i])
            if Sum>maximum:
                maximum=Sum
            i+=1
        return maximum
                
