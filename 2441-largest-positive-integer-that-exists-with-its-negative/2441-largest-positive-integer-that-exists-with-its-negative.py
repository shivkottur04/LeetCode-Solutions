class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        while nums:
            x=max(nums)
            if -x in nums:
                return x
            else:
                nums.remove(x)
        return -1