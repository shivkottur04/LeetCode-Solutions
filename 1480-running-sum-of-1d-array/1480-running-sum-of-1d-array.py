class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lst=[]
        for i in range(len(nums)):
            lst.append(sum(nums[:i+1]))
        return lst