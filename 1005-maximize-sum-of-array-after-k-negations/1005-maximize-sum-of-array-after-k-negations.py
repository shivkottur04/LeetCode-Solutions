class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        i=0
        while i<k:
            x=min(nums)
            n=nums.index(x)
            nums[n]*=-1
            i+=1
        return sum(nums)
        