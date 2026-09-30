class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        val=0
        for i in range(len(nums)):
            if i%2==0:
                val+=nums[i]
            else:
                val-=nums[i]
        return val