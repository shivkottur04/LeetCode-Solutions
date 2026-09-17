class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for x in range(len(nums)+1):
            count=0
            for i in nums:
                if i>=x:
                    count+=1
            if count==x:
                return x
        return -1

