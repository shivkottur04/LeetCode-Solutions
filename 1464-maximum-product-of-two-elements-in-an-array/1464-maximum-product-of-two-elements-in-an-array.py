class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums.sort()
        if len(nums)==1:
            return nums[0]
        return (nums[-1]-1)*(nums[-2]-1)