class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        nums[1::2]=sorted(nums[1::2],reverse=True)
        nums[0::2]=sorted(nums[0::2])
        return nums